from django.apps import AppConfig


class ActiviteConfig(AppConfig):
    name = 'activite'

    def ready(self):
        import activite.signals