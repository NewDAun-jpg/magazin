from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def about(request):#страница 'о нас'
    return render(request, 'core/about.html')

def contact(request):#страница 'контакты'
    return render(request, 'core/contact.html')

def register_view(request):#регистрация пользователей
    if request.method == 'POST':
        password = request.POST.get('password')
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            messages.error(request,'ошибка реализации вашей идеи')
            return render(request, 'core/register_view.html')
        else: #если нет пользователя то пересылает на его создание
            create_user = User.objects.create_user(username=username, password=password)
            return redirect('products:home')
    else:
        return render(request, 'core/register_view.html')
@login_required
def profile(request):
    if request.method == 'POST':

        pass