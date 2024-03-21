from django.apps import AppConfig


class InfluensysConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'influensys'
    def ready(self):
        import influensys.api.signals