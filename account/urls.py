from django.contrib.auth.views import AuthenticationForm, LoginView, LogoutView
from .views import LoginViews, LogoutViews, signup

from django.urls import path

urlpatterns = [
    path('login/', LoginViews.as_view(), name='login'),
    path('logout/', LogoutViews.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
]

