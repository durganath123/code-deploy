
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
#from authapp import views
from django.contrib.auth.views import LoginView
from chat import views as chat_views
from chatReg import views as reg_views
from django.contrib.auth.views import LoginView,LogoutView



urlpatterns = [
    path('',include('chatReg.urls')),

  
    path('admin/', admin.site.urls),

]

