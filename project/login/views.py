from django.shortcuts import render, redirect
from testApp.models import Student


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username and password match a student in the database
        student = Student.objects.filter(username=username, password=password).first()

        if student:
            request.session['student_id'] = student.id  # Store student ID in session
            return redirect('home')  # this will be changed to the student home page once it is created
        else:
            return render(request, 'login/login.html', {
                'error': "Invalid username or password."
            })

    return render(request, 'login/login.html')
