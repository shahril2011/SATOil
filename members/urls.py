from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name=""),
    path('register', views.register, name="register"),
    path('member_login', views.member_login, name="member_login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('member_logout', views.member_logout, name="member_logout"),
    path('analyze', views.sentiment_analysis, name="sentiment_analysis"),
    path('reset-password/', views.reset_password, name='reset_password'),
    path('set-new-password/', views.set_new_password, name='set_new_password'),
]
