from django.urls import path

from todo.views import TodoListView, TodoDetailView

urlpatterns = [
    path('list/', TodoListView.as_view()),
    path('detail/<int:pk>', TodoDetailView.as_view()),
]
