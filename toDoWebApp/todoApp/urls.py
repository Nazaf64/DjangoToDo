from django.urls import path
from . import views

urlpatterns = [
    path('', views.ToDoList, name='todolist'),
    # path('addTodo/', views.addToDo, name='addToDo'),
]

