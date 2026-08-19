from django.shortcuts import render, redirect, get_object_or_404
from classes.models import Class

def class_list(request):
    if request.method == 'POST':
        print(">>> USING CLASSES VIEW <<<")
        name = request.POST.get('name')
        code = request.POST.get('code')
        section = request.POST.get('section')

        if name and code and section:
            Class.objects.create(
                name=name,
                code=code,
                section=section
            )
        return redirect('class_list')

    classes = Class.objects.all()
    return render(request, 'classes/class_list.html', {'classes': classes})

def delete_class(request, class_id):
    class_obj = get_object_or_404(Class, id=class_id)
    class_obj.delete()
    return redirect('class_list')
