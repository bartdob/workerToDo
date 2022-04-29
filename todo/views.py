from django.shortcuts import render
from .models import Task, Worker
from django.http import HttpResponseRedirect


def workers(request):
    all_workers = Worker.objects.all()

    return render(request, 'todo/workers.html', {'all_workers': all_workers, })


def worker_del(request, worker_id):
    worker_to_del = Worker.objects.get(id=worker_id)
    worker_to_del.delete()
    return HttpResponseRedirect('/')


def worker_details(request, worker_id):
    worker = Worker.objects.get(id=worker_id)
    return render(request, 'todo/worker_details.html', {'worker': worker})



def todo(request):
    all_workers = Worker.objects.all()
    all_todo_items = Task.objects.all()

    print(Task.objects.all())

    return render(request, 'todo/todo.html', {'all_items': all_todo_items, 'all_workers': all_workers,})


def addTodo(request):
    new = Task(content=request.POST['content'], owner_id= request.POST['worker_id'])
    if len(request.POST['content']) > 2:
        new.save()
    return HttpResponseRedirect('/')


def deleteTodo(request, task_id):
    item_to_del = Task.objects.get(id=task_id)
    item_to_del.delete()
    return HttpResponseRedirect('/')
