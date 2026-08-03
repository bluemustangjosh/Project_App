from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Class

@login_required
def class_list(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Class.objects.create(student=request.user, name=name)
        return redirect('class_list')

    classes = Class.objects.filter(student=request.user)
    return render(request, 'classes/class_list.html', {'classes': classes})

@login_required
def delete_class(request, class_id):
    course = get_object_or_404(Class, id=class_id, student=request.user)
    course.delete()
    return redirect('class_list')