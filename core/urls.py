from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('record/', views.record, name='record'),
    path('client/<int:pk>/', views.client, name='client'),
    path('delete_client/<int:pk>/', views.delete_client, name='delete_client'),
    path('update_client/<int:pk>/', views.update_client, name='update_client'),
    path('add_client/', views.add_client, name='add_client'),
    path('download/', views.csv_record, name='download_record'),
    path('upload/', views.upload_csv_record, name='upload_record'),
]