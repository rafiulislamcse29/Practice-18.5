from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='homepage'),
    path('signup/', views.signup,name='signup_page'),
     path('login/', views.userlogin,name='loginpage'),
    path('profile/', views.profile,name='profilepage'),
     path('logout/', views.user_logout,name='logout'),
    path("pass_chnage/",views.pass_change,name='pass_change'),
    path("pass_chnage2/",views.pass_change2,name='pass_change2')

]
