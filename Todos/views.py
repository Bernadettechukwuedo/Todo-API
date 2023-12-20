from rest_framework import generics, status
from .serializer import TodoCreateSerializer, TodoSerializer
from .models import Todo
from rest_framework.response import Response


# Create your views here.


class CreateTodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    model = Todo
    serializer_class = TodoCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = TodoCreateSerializer(data=request.data)
        user = self.request.user

        if serializer.is_valid():
            todo = serializer.create(serializer.validated_data, user=user)
            read_serializer = self.get_serializer(todo)
            return Response(read_serializer.data, status=status.HTTP_201_CREATED)


# writing a code to list the todos
class ListTodo(generics.ListAPIView):
    model = Todo

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    serializer_class = TodoSerializer


# deleting todo
class DeleteTodo(generics.DestroyAPIView):
    model = Todo

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    serializer_class = TodoSerializer


class UpdateTodo(generics.UpdateAPIView):
    model = Todo

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    serializer_class = TodoSerializer
