from django.urls import path
from . import views

urlpatterns = [
    
    path('create', views.create,name='create'),
    path('', views.home,name='home'),
    path('show', views.show,name='show'),
    path('ashow', views.ashow,name='ashow'),  
    path('delete', views.delete1, name='delete'),
    path('update', views.update1, name='update'),
    path('update1', views.update2, name='update1'),
    
    
]