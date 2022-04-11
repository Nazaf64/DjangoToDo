from django.shortcuts import render, redirect
from .models import TodoList
from .forms import ToDoForm

# Create your views here.
def ToDoList(request):
    form = ToDoForm()
    todos = TodoList.objects.all()

    # context = {
    #     'todos': todos,
    #     'form': form
    # }

    # if request.method == 'POST':
    #     # print(request.POST)
    #     form = ToDoForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         # form = ToDoForm()
    #         return redirect('todo.html', context)
            
    context = {
        'todos': todos,
        'form': form
    }
    # return render(request, 'todoApp/todo.html', context)
    return render(request, 'todoApp/todoList.html', context)


# def addToDo(request):
#     form = ToDoForm()

#     if request.method == 'POST':
#         # print(request.POST)
#         form = ToDoForm(request.POST)
#         if form.is_valid():
#             form.save()
#         # form = ToDoForm()
#         return redirect('todo.html', context)
#     context = {
#         'form': form
#     }
#     return render(request, 'todoApp/todo.html', context)