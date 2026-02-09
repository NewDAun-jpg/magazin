from django.contrib.auth import get_user_model
from django.db.models.signals import post_save #сохраняет все после save()
from django.dispatch import receiver #привязывает вюьюху к сигналу
from .models import Profile #модель пользователя
from django.contrib.auth.models import User

User = get_user_model() #берем существующуу модель

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    #sender - модель, которая отправила сигнал (User)
    #instance - конкретный сохраненный объект (конкретный пользователь)
    #created - True если объект создан, False если обновлен
    #**kwargs - дополнительные аргументы
    if created:
        User.objects.create(username=instance.username, email=instance.email)

def create_user_profilee(sender, instance, created, **kwargs):
    if not created:
        print(f'ользователь обновлеНН {instance.username}')

