from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    #sender - модель, которая отправила сигнал (User)
    #instance - конкретный сохраненный объект (конкретный пользователь)
    #created - True если объект создан, False если обновлен
    #**kwargs - дополнительные аргументы
    if created:
        User.objects.create(username=instance.username, email=instance.email)