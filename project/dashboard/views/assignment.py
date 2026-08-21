# dashboard/views/assignment.py

from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from ..models import Assignment
from classes.models import Class
from testApp.models import Student


def get_logged_in_student(request):
    student_id = request.session.get('student_id')

    if not student_id:
        return None

    return Student.objects.filter(id=student_id).first()


def add_assignment(request):
    student = get_logged_in_student(request)

    if not student:
        return redirect('login')

    if request.method == 'POST':
        title = request.POST.get('title')
        class_id = request.POST.get('class_id')
        due_date = request.POST.get('due_date')
        description = request.POST.get('description', '')
        priority = request.POST.get('priority', 'medium')
        points = request.POST.get('points', 100)

        class_assigned = get_object_or_404(Class, id=class_id)

        Assignment.objects.create(
            title=title,
            description=description,
            class_assigned=class_assigned,
            due_date=due_date,
            priority=priority,
            points=points,
            created_by=request.user,
            status='pending'
        )

        return redirect('dashboard:home')

    return redirect('dashboard:home')


def toggle_assignment_complete(request, assignment_id):
    student = get_logged_in_student(request)

    if not student:
        return redirect('login')

    if request.method == 'POST':
        assignment = get_object_or_404(Assignment, id=assignment_id)

        if assignment.status == 'completed':
            assignment.status = 'pending'
        else:
            assignment.status = 'completed'

        assignment.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False}, status=400)


def delete_assignment(request, assignment_id):
    student = get_logged_in_student(request)

    if not student:
        return redirect('login')

    if request.method == 'POST':
        assignment = get_object_or_404(Assignment, id=assignment_id)
        assignment.delete()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False}, status=400)