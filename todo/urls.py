from django.urls import path, include

from todo.views import todo_view

urlpatterns = [
    path('', todo_view),
]
