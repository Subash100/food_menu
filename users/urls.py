from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as authentication_views


app_name= 'users'
urlpatterns = [
    path('',views.register, name="register"),
    path('login/',authentication_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    #path('logout/',authentication_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('logout/',views.logout_view,name='logout'),
    path('profile/',views.profilepage, name="profile"),
]

# urlpatterns += [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)