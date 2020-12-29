from django.db import models


class Task(models.Model):
    subject = models.CharField(max_length=20)
    task1 = models.CharField(max_length=100, blank=True, default='✔')
    task2 = models.CharField(max_length=100, blank=True, default='✔')
    task3 = models.CharField(max_length=100, blank=True, default='✔')
    task4 = models.CharField(max_length=100, blank=True, default='✔')
    task5 = models.CharField(max_length=100, blank=True, default='✔')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
