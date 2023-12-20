from django.urls import path
from .views import CreateTodo, ListTodo, DeleteTodo, UpdateTodo

app_name = "Todos"
urlpatterns = [
    path("create/", CreateTodo.as_view(), name="api_create"),
    path("list/", ListTodo.as_view(), name="api_list"),
    path("delete/<int:pk>", DeleteTodo.as_view(), name="api_delete"),
    path("update/<int:pk>", UpdateTodo.as_view(), name="api_update"),
]
