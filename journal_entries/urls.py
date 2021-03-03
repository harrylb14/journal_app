from django.urls import path

from . import views

app_name = 'journal_entries'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.create_resource_ajax, name='ajax_create'),
    path('edit/<int:resource_id>/', views.update_resource_ajax, name='ajax_update'),
    path('delete/<int:resource_id>/', views.delete_resource_ajax, name='ajax_delete'),
    path('ajax_search/', views.ajax_search, name='ajax_search'),
]
