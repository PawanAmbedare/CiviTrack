from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report/', views.report_pothole, name='report_pothole'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('report/<int:pk>/update_status/', views.update_status, name='update_status'),
]
