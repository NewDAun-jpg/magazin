from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def register_view(request):#регистрация пользователя
    if request.method == 'POST':
        password = request.POST.get('password')
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            return HttpResponse('имя занято,даун')#Проверить, нет ли такого пользователя
        else:
            create_user = User.objects.create_user(username=username, password=password)
            return redirect('products:home')
    else:
        return render(request, 'core/register_view.html')

def login_view(request):
    return render(request, 'core/login.html')