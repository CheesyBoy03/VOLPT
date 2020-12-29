from django.db import models


class Day(models.Model):
    """day_number = models.IntegerField()
    day_of_week = models.CharField(max_length=20)
    subjects = models.TextField()"""

    day_number = models.CharField(max_length=2)
    day_of_week = models.CharField(max_length=20)
    subject_1 = models.CharField(max_length=50, default="-")
    subject_2 = models.CharField(max_length=50, default="-")
    subject_3 = models.CharField(max_length=50, default="-")
    subject_4 = models.CharField(max_length=50, default="-")

    def __str__(self):
        return self.day_of_week
