from django.views.generic import ListView
from todo.models import TodoModel


class TodoListView(ListView):
    template_name = 'list.html'
    model = TodoModel
