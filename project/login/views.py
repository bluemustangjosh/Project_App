from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.views.decorators.cache import never_cache
from testApp.models import Student


def _render_auth(request, *, active_panel='login', **context):
    """Render every account task in the same StudyDesk screen."""
    return render(request, 'login/login.html', {
        'active_panel': active_panel,
        'next': request.POST.get('next') or request.GET.get('next', ''),
        **context,
    })


@never_cache
def login_view(request):
    # If already logged in using Student session
    if request.session.get('student_id'):
        return redirect('class_list')

    if request.method == 'POST':
        identifier = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        # Allow login by username OR email
        student = Student.objects.filter(username__iexact=identifier, password=password).first()
        if student is None:
            student = Student.objects.filter(email__iexact=identifier, password=password).first()

        if student:
            request.session['student_id'] = student.id
            return redirect(request.POST.get('next') or 'class_list')

        return _render_auth(
            request,
            active_panel='login',
            error="Your email/username and password didn't match. Please try again.",
            login_identifier=identifier,
        )

    return _render_auth(request, active_panel='login')



@never_cache
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('class_list')

    if request.method != 'POST':
        return _render_auth(request, active_panel='signup')

    username = request.POST.get('username', '').strip()
    email = request.POST.get('email', '').strip()
    password = request.POST.get('password', '')
    confirm_password = request.POST.get('password_confirm', '')
    errors = []

    if not username:
        errors.append('Please choose a username.')
    elif User.objects.filter(username__iexact=username).exists():
        errors.append('That username is already in use.')
    if not email:
        errors.append('Please enter your email address.')
    elif User.objects.filter(email__iexact=email).exists():
        errors.append('An account already uses that email address.')
    if password != confirm_password:
        errors.append('The two passwords do not match.')
    else:
        try:
            validate_password(password, user=User(username=username, email=email))
        except ValidationError as validation_error:
            errors.extend(validation_error.messages)

    if errors:
        return _render_auth(request, active_panel='signup', errors=errors,
                            signup_username=username, signup_email=email)

    user = User.objects.create_user(username=username, email=email, password=password)
    login(request, user)
    return redirect(request.POST.get('next') or 'class_list')


def signup_view(request):
    # If already logged in using Student session
    if request.session.get('student_id'):
        return redirect('class_list')

    # If GET request, show signup panel
    if request.method != 'POST':
        return _render_auth(request, active_panel='signup')

    # Collect form fields
    first_name = request.POST.get('first_name', '').strip()
    last_name = request.POST.get('last_name', '').strip()
    student_id = request.POST.get('student_id', '').strip()
    username = request.POST.get('username', '').strip()
    email = request.POST.get('email', '').strip()
    password = request.POST.get('password', '')
    confirm_password = request.POST.get('password_confirm', '')

    errors = []

    # Validate required fields
    if not first_name:
        errors.append("Please enter your first name.")
    if not last_name:
        errors.append("Please enter your last name.")
    if not student_id:
        errors.append("Please enter your student ID.")

    if not username:
        errors.append("Please choose a username.")
    elif Student.objects.filter(username__iexact=username).exists():
        errors.append("That username is already in use.")

    if not email:
        errors.append("Please enter your email address.")
    elif Student.objects.filter(email__iexact=email).exists():
        errors.append("An account already uses that email address.")

    if password != confirm_password:
        errors.append("The two passwords do not match.")

    # If errors, re-render signup page
    if errors:
        return _render_auth(
            request,
            active_panel='signup',
            errors=errors,
            signup_username=username,
            signup_email=email
        )

    # Create Student (NOT Django User)
    student = Student.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        student_id=student_id,
        username=username,
        password=password
    )

    # Custom login using session
    request.session['student_id'] = student.id

    return redirect(request.POST.get('next') or 'class_list')


def password_reset_confirm_view(request, uidb64, token):
    """Complete the email-link reset inside the same authentication template."""
    try:
        user = User.objects.get(pk=force_str(urlsafe_base64_decode(uidb64)))
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is None or not default_token_generator.check_token(user, token):
        return _render_auth(request, active_panel='login',
                            error='That password-reset link is invalid or has expired.')

    if request.method == 'POST':
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('password_confirm', '')
        errors = []
        if password != confirm_password:
            errors.append('The two passwords do not match.')
        else:
            try:
                validate_password(password, user=user)
            except ValidationError as validation_error:
                errors.extend(validation_error.messages)
        if not errors:
            user.set_password(password)
            user.save()
            return _render_auth(request, active_panel='login',
                                success='Your password has been reset. You can now log in.')
        return _render_auth(request, active_panel='new-password', errors=errors,
                            reset_confirm_url=request.path)

    return _render_auth(request, active_panel='new-password', reset_confirm_url=request.path)

# login/views.py
@never_cache
def password_reset_request_view(request):
    """First step of password reset — just needs a URL to exist so the form doesn't 404/crash."""
    if request.method == 'POST':
        # Not actually emailing anything — just acknowledge and send them back to login.
        return _render_auth(
            request, active_panel='login',
            success='If that email is registered, a reset link would be sent (demo only).'
        )

    return _render_auth(request, active_panel='reset')