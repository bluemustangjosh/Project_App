from django.shortcuts import render, redirect
from testApp.models import Student, Class

def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username and password match a student in the database
        student = Student.objects.filter(username=username, password=password).first()

        if student:
            request.session['student_id'] = student.id  # Store student ID in session

            # NEW LOGIC: check if student has classes
            if student.classes.count() == 0:
                return redirect('class_list')
            else:
                return redirect('home')

        else:
            return render(request, 'login/login.html', {
                'error': "Invalid username or password."
            })

    # IMPORTANT: this must exist for GET requests
    return render(request, 'login/login.html')


def class_list_view(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('login')

    student = Student.objects.get(id=student_id)

    # Only this student's classes
    classes = student.classes.all()

    return render(request, 'classes/class_list.html', {
        'student': student,
        'classes': classes
    })

def add_class_view(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('login')

    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        code = request.POST.get('code')
        section = request.POST.get('section')

        print(">>> ADD CLASS POST FIRED <<<")
        print("name:", name, "code:", code, "section:", section)

        if name and code and section:
            new_class = Class.objects.create(
                name=name,
                code=code,
                section=section
            )
            student.classes.add(new_class)

        return redirect('class_list')

    return render(request, 'classes/add_class.html')


def landing(request):
    return render(request, 'home/home.html')


def home(request):
    ...
