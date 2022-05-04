from django.shortcuts import render
from .models import Task, Worker
from django.http import HttpResponseRedirect
from .filters import TaskFilter


def workers(request):
    all_workers = Worker.objects.all()

    return render(request, 'todo/workers.html', {'all_workers': all_workers, })


def worker_del(request, worker_id):
    worker_to_del = Worker.objects.get(id=worker_id)
    worker_to_del.delete()
    return HttpResponseRedirect('/')


def worker_details(request, worker_id):
    worker = Worker.objects.get(id=worker_id)
    tasks = worker.task_set.all()
    myFilter = TaskFilter(request.GET, queryset=tasks)
    tasks = myFilter.qs
    context = {'worker': worker,'tasks': tasks, 'myFilter': myFilter}
    return render(request, 'todo/worker_details.html', context)


def addWorker(request):
    new = Worker(
        forename=request.POST['forename'],
        surname=request.POST['surname'],
        age=request.POST['age'],
        content=request.POST['content'],

    )
    if len(request.POST['forename'] and request.POST['surname']) > 2:
        new.save()
    return HttpResponseRedirect('/')


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
