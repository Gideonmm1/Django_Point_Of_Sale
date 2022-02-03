from django.urls import path

from login.views import LoginPageView

urlpatterns = [
    path('login', LoginPageView.as_view(), name='login'),
]