from django.db import models
from django.db.models import DateField
from django.utils import timezone


class Worker(models.Model):
    forename = models.CharField(max_length=80)
    surname = models.CharField(max_length=80)
    date_od_birth = models.DateField(null=True)
    age = models.IntegerField(default=None)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.surname


class Task(models.Model):
    TASK_STATUS = [('FR', 'FRESH'), ('IP', 'InPROGRESS'), ('DONE', 'DONE')]
    owner = models.ForeignKey(Worker, on_delete=models.CASCADE)
    content = models.TextField()
    done = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(choices=TASK_STATUS, default='FRESH', max_length=80)

    def __str__(self):
        return self.content
