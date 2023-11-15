from django.urls import path
from . import views

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('home/',views.TaskListview.as_view(),name='home'),
    path('details/',views.TaskDetailview.as_view(),name='details'),
    path('register/',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout/',views.logout,name='logout'),


]
