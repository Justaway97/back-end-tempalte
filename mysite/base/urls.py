from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'home', views.home, name='home'),
    path(r'option', views.option, name='option'),
    path(r'home/update', views.homeUpdate, name='homeUpdate'),
    path(r'table', views.table, name='table'),
    path(r'table/update', views.tableUpdate, name='tableUpdate'),
    path(r'table/add', views.tableAdd, name='tableAdd'),
    path(r'table/delete', views.tableDelete, name='tableDelete')
]