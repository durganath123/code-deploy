
from django.urls import path,include
from django.conf.urls import url
from chatReg import views as reg_views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('dashboard/', reg_views.dashboard,name='dashboard'),

    path('',LoginView.as_view(), name='login_url' ),
    path('logout/',LogoutView.as_view(next_page='login_url'),name='logout'),

    path('chat/', reg_views.chat_index, name='chat_index'),
    path('chat/<str:room_name>/', reg_views.chat_room, name='room'),

    path('signup/', reg_views.signup, name='register_url'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        reg_views.activate, name='activate'),

    url('', include('django.contrib.auth.urls')),
  
]

