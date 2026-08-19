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

            # NEW LOGIC: check if student has classes
            if student.classes.count() == 0:
                return redirect('class_list')   # send them to class_list.html
            else:
                return redirect('home')         # send them to home page

        else:
            return render(request, 'login/login.html', {
                'error': "Invalid username or password."
            })

    return render(request, 'login/login.html')
