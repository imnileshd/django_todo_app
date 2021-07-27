from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm

# Create your views here.

class TodoList(generic.ListView): 
    model = Todo

class TodoDetail(generic.DetailView): 
    model = Todo

class TodoCreate(generic.CreateView): 
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')

class TodoUpdate(generic.UpdateView): 
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')

class TodoDelete(generic.DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')