from django.urls import path
from . import views

app_name = 'sale'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('report/', views.report, name='report'),
    path('register/', views.register, name='register'),
    path('completed/', views.completed, name='completed'),
    # path('register/get_name', views.get_name, name='registered'),

]
