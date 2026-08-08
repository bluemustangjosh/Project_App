from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_view(request):
    if request.user.is_authenticated:
        return redirect('chat_home')  # wherever your homework-chat dashboard lives

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or 'chat_home'
            return redirect(next_url)
        else:
            return render(request, 'testApp/login.html', {
                'error': "Your username and password didn't match. Please try again."
            })

    return render(request, 'testApp/login.html')