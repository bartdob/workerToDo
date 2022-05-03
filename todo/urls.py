from django.urls import path
from . import views


urlpatterns = [
    path('', views.todo, name='todo'),
    path('addTodo/new/', views.addTodo, name='addTodo'),
    path('deleteTodo/<int:task_id>/', views.deleteTodo, name='deleteTodo'),
    path('workers/', views.workers, name='all_workers'),
    path('workers/details/<int:worker_id>/', views.worker_details, name='worker_details'),
    path('workers/worker_del/<int:worker_id>/', views.worker_del, name='worker_del'),
    path('workers/addWorker/new/', views.addWorker, name='addWorker')
]