from django.apps import AppConfig


class PricemonitorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pricemonitor'

    
    def ready(self):
        import pricemonitor.signals
