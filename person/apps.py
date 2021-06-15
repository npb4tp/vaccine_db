from django.apps import AppConfig


class PersonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'person'
    
    def ready(self):
        """Call the ready method and connect receiver when database is connected """
        super(PersonConfig, self).ready()
        import person.signals

