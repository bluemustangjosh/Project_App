from django.shortcuts import render, redirect
from testApp.models import Student, Class

# Create your views here.
def add_class_view(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('login')  # sending to login page if student is not logged in
    student = Student.objects.get(id=student_id)
    
    if request.method == 'POST':
        class_id = request.POST.get('class_id')
        if class_id:
            selected_class = Class.objects.get(id=class_id)
            student.classes.add(selected_class)
            student.save()
            return redirect('home')  # redirecting to home page after adding class
    
    all_classes = Class.objects.all()
    return render(request, 'classes/class_list.html', {'all_classes': all_classes})