from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LogView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<str:username>/', views.ProfileView.as_view(),
         name='profile'),
    path('profile/edit/', views.ProfileUpdateView.as_view(),
         name='profile_edit'),
    path('password/change/', views.CustomPasswordChangeView.as_view(),
         name='password_change'),
    path('password_reset/', include('django.contrib.auth.urls')),
]
