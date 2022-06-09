from django import views
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('login/', views.loginPage,name="loginpage"),
    path('logout/', views.userout,name="logout"),
    path('register/', views.registerPage,name="registerpage"),
    path('records/', views.records,name="records"),
    path('mystudent/', views.mystudent,name="mystudents"),
    path('attendace/', views.attend,name="attendace"),
    path('myinfo/', views.myinfo,name="myinfo"),
    path('manage/', views.managerec,name="manage"),
    path('manage/edit/<int:pk>/', views.studentedit,name="studentedit"),
    path('manage/delete/<int:pk>/', views.studentdel,name="studentdel"),
    path('student/add/', views.addstudent,name="addstudent"),
    
]