from django.urls import path
from userApp import views

urlpatterns = [
    path('', views.main),
    path('error', views.error_page),
    path('user', views.user_info),
    path('user/<slug:login>', views.user_info),
    path('user/<slug:login>/<slug:post_name>', views.user_info),
    path('user/<slug:login>/<slug:post_name>/<int:post_number>', views.user_info),
]
