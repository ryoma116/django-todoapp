from django.views.generic import ListView, DetailView

from todo.models import TodoModel


class TodoListView(ListView):
    template_name = 'list.html'
    model = TodoModel


class TodoDetailView(DetailView):
    template_name = 'detail.html'
    model = TodoModel
