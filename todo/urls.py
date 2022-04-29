from django.urls import path
from . import views


urlpatterns = [
    path('', views.todo, name='todo'),
    path('addTodo/new/', views.addTodo, name='addTodo'),
    path('deleteTodo/<int:todo_id>/', views.deleteTodo, name='deleteTodo'),
    path('workers/', views.workers, name='all_workers'),
    path('worker_del/<int:worker_id>/', views.worker_del, name='workers_del'),
]