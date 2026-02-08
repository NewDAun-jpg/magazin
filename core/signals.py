from django.contrib.auth import get_user_model
from django.db.models.signals import post_save #сохраняет все после save()
from django.dispatch import receiver #привязывает вюьюху к сигналу
from .models import pass #модель пользователя

User = get_user_model() #берем существующуу модель

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs): #модель отправивший сигнал, конкретный сохраненный обьект,
