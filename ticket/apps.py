from django.apps import AppConfig
from ticket import views



class TicketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ticket'
