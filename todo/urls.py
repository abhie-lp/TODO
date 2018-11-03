from django.urls import path
from . import views

urlpatterns = [
    path("", views.TodoListView.as_view(), name="todo_list"),
    path("new/", views.TodoCreateView.as_view(), name="todo_create"),
    path("do/<int:pk>/delete/", views.TodoDeletView.as_view(), name="todo_delete"),
]