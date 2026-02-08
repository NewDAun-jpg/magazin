from django.apps import AppConfig


class ProductsConfig(AppConfig):
    name = 'products'

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

    def ready(self):
        import user.signals
