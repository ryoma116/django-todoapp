from django.urls import path

from todo.views import TodoListView

urlpatterns = [
    path('list/', TodoListView.as_view()),
]
