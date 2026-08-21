from django.shortcuts import render, redirect, get_object_or_404
from classes.models import Class
from testApp.models import Student

def class_list(request):
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


def delete_class(request, class_id):
    class_obj = get_object_or_404(Class, id=class_id)
    class_obj.delete()
    return redirect('class_list')
