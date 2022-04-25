from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view/<int:pantry_id>/', views.pantry_view, name='pantry_view'),
    path('register/', views.user_auth, name='user_auth'),
    path('register/<int:user_id>/pantry-form/', views.pantry_creation, name='pantry_creation'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]
