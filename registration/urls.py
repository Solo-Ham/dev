from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(success_url='/vacs/'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('confirm/', views.confirm_email, name='confirm')
]

# path('logout/', LogoutView.as_view(next_page='/vacs/'), name='logout'