from django.shortcuts import render
from django.urls import reverse_lazy


# Create your views here.
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Task

class TaskList(ListView):
    model = Task
    template_name = "todo/task_list.html"
    context_object_name = "tasks"
    

class CreateTask(CreateView):
    model = Task
    template_name = "todo/create_task.html"
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    

class TaskDetail(DetailView):
    model = Task
    template_name = "todo/task_detail.html"
    context_object_name = "task"