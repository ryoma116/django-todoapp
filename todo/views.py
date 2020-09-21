from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from todo.models import TodoModel


class TodoListView(ListView):
    template_name = 'list.html'
    model = TodoModel


class TodoDetailView(DetailView):
    template_name = 'detail.html'
    model = TodoModel


class TodoCreateView(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')


class TodoDeleteView(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')
