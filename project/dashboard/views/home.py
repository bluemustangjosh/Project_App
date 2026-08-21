# dashboard/views/home.py
from django.shortcuts import render, redirect
from testApp.models import Student
from ..models import Assignment


def dashboard_view(request):
    student_id = request.session.get('student_id')

    if not student_id:
        return redirect('login')

    student = Student.objects.get(id=student_id)
    classes = student.classes.all()

    upcoming_assignments = Assignment.objects.filter(
        class_assigned__in=classes
    ).exclude(status='completed').order_by('due_date')

    # Build calendar markers: "YYYY-M-D" -> class name (used for dot color)
    calendar_events = {}
    for a in upcoming_assignments:
        key = f"{a.due_date.year}-{a.due_date.month}-{a.due_date.day}"
        calendar_events[key] = a.class_assigned.name

    return render(request, 'dashboard/home.html', {
        'student': student,
        'classes': classes,
        'upcoming_assignments': upcoming_assignments,
        'calendar_events': calendar_events,
    })