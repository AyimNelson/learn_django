from django.urls import path
from .views import TaskList, CreateTask, TaskDetail, UpdateTask


urlpatterns=[
    path('', TaskList.as_view(), name='tasks'),
    path('task/create', CreateTask.as_view(), name='create_task'),
    path('task/detail/<str:pk>/', TaskDetail.as_view(), name='task'),
    path('task/update/<str:pk>/', UpdateTask.as_view(), name='update_task'),
]