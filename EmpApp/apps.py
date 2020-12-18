from django.apps import AppConfig


class EmpappConfig(AppConfig):
    name = 'EmpApp'


    def ready(self):
        import EmpApp.signals
