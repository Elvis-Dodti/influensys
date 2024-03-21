from django.apps import AppConfig


class BuisnessConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'buisness'

    def ready(self):
        import buisness.api.signals
