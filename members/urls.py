from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name=""),
    path('register', views.register, name="register"),
    path('member_login', views.member_login, name="member_login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('member_logout', views.member_logout, name="member_logout")
]
