from django.contrib import admin
from django.urls import path,include
from crudmainapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('test/',views.test),
    path('insert/',views.insert,name="insert"),
    path('insertdata/',views.InsertData, name="insertdata"),
    path('tabledata/',views.showtable,name="showtable"),
    path('showdata/',views.showdata,name="showdata"),
    path('editdata/<int:pk>/',views.editdata,name='editdata'),
    path('updatedata/<int:pk>/',views.updatedata,name='updatedata'),
    path('deletedata/<int:pk>/',views.deletedata,name='deletedata'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.signuppage,name='signup'),
    path('logout/',views.logout,name='logout'),
]