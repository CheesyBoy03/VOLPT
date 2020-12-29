from django.shortcuts import render, redirect
from .forms import *


def todo_view(request):
    tasks = Task.objects.all()  # Если надо перевернуть список, то просто добавь после .all() [::-1]

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('Error'*10)       # Для отладки валидности введенных данных
        return redirect('/todo/')
    else:
        form = TaskForm()

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/todo.html', context)
