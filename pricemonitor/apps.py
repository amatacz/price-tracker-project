from django.apps import AppConfig


class PricemonitorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pricemonitor'

<<<<<<< HEAD
    
    def ready(self):
        import pricemonitor.signals
=======
    def ready(self):
        import pricemonitor.signals
>>>>>>> 83c5cfa6f4e0dd156aa2811706d5d49ab811c8c4
