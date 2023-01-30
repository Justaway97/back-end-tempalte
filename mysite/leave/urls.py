from django.urls import path
from . import views
from base import views as baseViews

urlpatterns = [
    path(r'login', baseViews.login, name='login'),
    path(r'code', baseViews.getCode, name='get code'),
    path(r'leave/summary', views.leaveSummary, name='leave summary'),
    path(r'leave/coming', views.leaveComing, name='coming leave'),
    path(r'leave/pending', views.leavePending, name='pending leave'),
    path(r'leave/history', views.leaveHistory, name='history leave'),
    # path(r'option', views.option, name='option'),
    # path(r'home/update', views.homeUpdate, name='homeUpdate'),
    # path(r'table', views.table, name='table'),
    # path(r'table/update', views.tableUpdate, name='tableUpdate'),
    # path(r'table/add', views.tableAdd, name='tableAdd'),
    # path(r'table/delete', views.tableDelete, name='tableDelete')
]