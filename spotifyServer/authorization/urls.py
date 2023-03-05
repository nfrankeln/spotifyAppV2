from . import views
from django.urls import path, re_path
app_name="autherization"
urlpatterns = [
    path('', views.index),
    path('api/register/',views.register),
    path('api/login/',views.user_login),
    path('api/logout/',views.user_logout),
    path('api/is_authenticated/',views.is_authenicated),
    re_path(r'.*', views.index)
]



    