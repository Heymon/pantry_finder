from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.user_auth, name='user_auth'),
    # path('signup/', views.signup, name='signup'),
    path('register/<int:user_id>/pantry-form/', views.pantry_creation, name='pantry_creation'),
]
