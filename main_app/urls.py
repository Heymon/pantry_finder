from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.user_auth, name='user_auth'),
    path('register/<int:user_id>/pantry-form/', views.pantry_creation, name='pantry_creation'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]
