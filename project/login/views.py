from django.shortcuts import render, redirect
from testApp.models import Student

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        student = Student.objects.filter(username=username, password=password).first()

        if student:
            request.session['student_id'] = student.id
            return redirect('home')
        else:
            return render(request, 'login/login.html', {
                'error': "Invalid username or password."
            })

    return render(request, 'login/login.html')
