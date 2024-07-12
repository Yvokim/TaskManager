from django.urls import path
from . import views

urlpatterns = [

    path('', views.task_list, name='task_list'),
    path('<int:pk>/', views.task_detail, name='task_detail'),
    path('<int:pk>/confirm_delete/', views.task_confirm_delete, name='task_confirm_delete'),
    path('new/', views.task_create, name='task_create'),
    path('<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('<int:task_pk>/subtasks/new', views.subtask_create, name='subtask_create'),
    path('<int:task_pk>/subtasks/<int:subtask_pk>/subtask_detail', views.subtask_detail, name='subtask_detail'),
    path('<int:task_pk>/subtasks/<int:subtask_pk>/edit/', views.subtask_edit, name='subtask_edit'),
    path('<int:task_pk>/subtasks/<int:subtask_pk>/delete', views.subtask_delete, name='subtask_delete'),
    path('<int:task_pk>/subtasks/<int:subtask_pk>/confirm_delete', views.subtask_confirm_delete,
         name='subtask_confirm_delete')
]
