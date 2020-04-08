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
    path('cars/<int:car_id>/add_maint/', views.add_maint, name='add_maint'),
    path('parts/', views.PartList.as_view(), name='part_index'),
    path('parts/<int:pk>/', views.PartDetail.as_view(), name='part_detail'),
    path('parts/create/', views.PartCreate.as_view(), name='part_create'),
    path('parts/<int:pk>/update/', views.PartUpdate.as_view(), name='part_update'),
    path('parts/<int:pk>/delete/', views.PartDelete.as_view(), name='part_delete'),
]