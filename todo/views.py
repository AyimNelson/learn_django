from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Task

class TaskList(ListView):
    model = Task
    template_name = "todo/task_list.html"
    context_object_name = "tasks"