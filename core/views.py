from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile

def about(request):#страница 'о нас'
    return render(request, 'core/about.html')

def contact(request):#страница 'контакты'
    return render(request, 'core/contact.html')

def register_view(request):#регистрация пользователей
    if request.method == 'POST':
        password = request.POST.get('password')
        username = request.POST.get('username')
        email = request.POST.get('email')
        if User.objects.filter(username=username).exists(): #не допустить повтора логина
            messages.error(request,'ошибка реализации вашей идеи')
            return render(request, 'core/register_view.html')
        else: #если нет пользователя то пересылает на его создание
            create_user = User.objects.create_user(username=username, password=password)
            return redirect('products:home')
    else:
        return render(request, 'core/register_view.html')



@login_required
def profile(request):#профиль
    if request.method == 'POST':
        # Получаем новые данные из формы
        new_username = request.POST.get('username')
        new_email = request.POST.get('email')
        # Обновляем данные текущего пользователя
        user = request.user
        user.username = new_username
        user.email = new_email
        user.save()
        # Перенаправляем на ту же страницу
        return redirect('core:profile')  #
    # Для GET запроса показываем форму с текущими данными
    return render(request, 'core/profile.html', {'user': request.user})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('products:home')
        else:
            return render(request, 'core/login_view.html')



