from django.shortcuts import render, redirect
from testApp.models import Student


def dashboard_view(request):
    student_id = request.session.get('student_id')

    if not student_id:
        return redirect('login')

    student = Student.objects.get(id=student_id)

    return render(request, 'dashboard/home.html', {
        'student': student,
    })