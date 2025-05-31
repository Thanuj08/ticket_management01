from django.contrib import admin
from django.urls import path
from . import views  # Correctly import your views module

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Home page
    path('', views.home, name='home'),

    # Authentication views
    path('signin/page/', views.signin_page, name='signin_page'),
    path('signup/page/', views.signup_page, name='signup_page'),

    # Ticket creation and history
    path('tickets/raise/', views.raise_ticket, name='raise_ticket'),
    path('tickets/history/', views.ticket_history, name='ticket_history'),

    # Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
