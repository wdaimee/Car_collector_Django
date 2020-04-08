from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.car_index, name='index'),
    path('cars/<int:car_id>/', views.car_detail, name='detail'),
    path('cars/create/', views.CarCreate.as_view(), name='car_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='car_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='car_delete'),
]