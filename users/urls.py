from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterUser, generate_new_password

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/genpassword', generate_new_password, name='generate_new_password'),
    path('register/', RegisterUser.as_view(), name='register'),
]