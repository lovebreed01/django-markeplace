from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('item/<slug:slug>/', views.details,name='details'),
    path('category/<slug:slug>/',views.category,name='category'),
    path('messages/',views.user_message,name='message'),

    path('create', views.item_create, name='create'),
    path('item/<slug:slug>/delete',views.item_del,name='delete'),
    path('item/ <slug:slug>/edit',views.item_edit,name='edit')
   

]