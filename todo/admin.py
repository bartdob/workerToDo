from django.contrib import admin
from .models import Worker, Task

admin.site.register(Task)
admin.site.register(Worker)
