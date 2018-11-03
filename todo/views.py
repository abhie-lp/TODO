from django.urls import reverse
from .models import Todo
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView


class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = "__all__"
    template_name = "todo/todo_list.html"


class TodoDeletView(DeleteView):
    model = Todo

    def get_success_url(self):
        return reverse("todo_list")
