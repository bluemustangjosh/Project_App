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
    all_classes = Class.objects.all()

    return render(request, 'classes/class_list.html', {
        'student': student,
        'all_classes': all_classes
    })

def add_class_view(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('login')

    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        class_id = request.POST.get('class_id')
        if class_id:
            selected_class = Class.objects.get(id=class_id)
            student.classes.add(selected_class)
            student.save()
            return redirect('home')

    all_classes = Class.objects.all()
    return render(request, 'classes/class_list.html', {'all_classes': all_classes})

def landing(request):
    return render(request, 'home/home.html')


def home(request):
    ...
