from django.shortcuts import render, redirect
from testApp.models import Student


def landing(request):
    return render(request, 'home/home.html')


def home(request):
    student_id = request.session.get('student_id')

    if not student_id:
        return redirect('login')

    student = Student.objects.get(id=student_id)

    if student.classes.count() == 0:
        return redirect('class_list')

    return render(request, 'home/home.html', {
        'student': student,
    })