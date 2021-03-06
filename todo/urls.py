from django.urls import path

from todo.views import TodoListView, TodoDetailView, TodoCreateView, TodoDeleteView, TodoUpdateView

urlpatterns = [
    path('list/', TodoListView.as_view(), name='list'),
    path('detail/<int:pk>', TodoDetailView.as_view(), name='detail'),
    path('create/', TodoCreateView.as_view(), name='create'),
    path('delete/<int:pk>', TodoDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', TodoUpdateView.as_view(), name='update'),
]
