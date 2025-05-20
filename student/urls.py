from django.contrib import admin
from django.urls import path
from  . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('add_student',views.add_student,name='add_student'),
     path('delete/<str:name>/', views.delete_student, name='delete_student'),
   path('update/<int:id>/', views.update_student, name='update_student'),
       path('register/', views.register_user, name='register_user'),
 path('login/', views.login_user, name='login')
]
