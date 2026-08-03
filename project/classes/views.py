from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Course

@login_required
def course_list(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Course.objects.create(name=name)
        return redirect('coruse_list')

    courses = Course.objects.filter(student=request.user)
    return render(request, 'classes/course_list.html', {'courses': courses})