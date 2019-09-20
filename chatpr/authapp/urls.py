from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

from authapp import views


urlpatterns = [

    path('',views.index, name='home'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('login/',LoginView.as_view(),name='login_url'),
    path('register/',views.register,name="register_url"),
    path('logout/',LogoutView.as_view(next_page='home'),name='logout'),

]