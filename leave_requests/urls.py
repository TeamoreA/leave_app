from django.urls import path

from . import views

urlpatterns = [
    path('', views.leave_index_view, name='index'),
    path('add/', views.create_leave_view, name='add_leave'),
    path('user/add/', views.create_user_view, name='add_user'),
    path('<int:leave_id>/update/', views.update_leave_view, name='update_leave'),
    path('<int:leave_id>/delete/', views.delete_leave_view, name='delete_leave')
]