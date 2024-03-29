from django.urls import path
from .views import TaskList, CreateTask


urlpatterns=[
    path('', TaskList.as_view(), name='tasks'),
    path('task/create', CreateTask.as_view(), name='create_task'),
]