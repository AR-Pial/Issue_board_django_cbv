from django.urls import path
from .views import HomeRedirectView, LoginFormView, LogoutFormView, RegisterFormView

urlpatterns = [
    path('', HomeRedirectView.as_view(), name='home'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutFormView.as_view(), name='logout'),
    path('register/', RegisterFormView.as_view(), name='register'),
]
