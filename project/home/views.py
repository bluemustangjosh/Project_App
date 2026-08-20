from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from testApp.models import Student

def landing(request):
    return render(request, 'home/home.html')

@login_required(login_url='login')
def home(request):
    student = Student.objects.filter(username=request.user.username).first()

    if student is None or student.classes.count() == 0:
        return redirect('add_class')

    return render(request, 'home/home.html')