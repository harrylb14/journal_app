from django.urls import path

from . import views

app_name = 'journal_entries'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete_resource'),
    path('create/', views.create_resource_ajax, name='ajax_create'),
]
