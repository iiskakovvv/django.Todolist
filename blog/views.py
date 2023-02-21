from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_POST

def index(request):
    todo = Todo.objects.all()
    form = TodoForm()
    context = {'todo_list':todo, 'form':form}
    return render(request, 'index.html', context)


def add_form(request):
    todo = Todo.objects.all()
    return render(request, 'add.html', {'todo_list':todo})

@require_POST
def add_todo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = Todo(title=request.POST['text'])
        new_todo.save()
    return redirect('/')
    

def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if todo.complate:
        todo.complate = False
        todo.save()
    else:
        todo.complate = True
        todo.save()
    return redirect('/')



def delete_all(request):
    Todo.objects.all().delete()
    return redirect('/')

def delete_completed(request):
    Todo.objects.filter(complate=True).delete()
    return redirect('/')

    

