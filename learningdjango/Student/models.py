from django.db import models


class StudentInfo(models.Model):
    name = models.CharField(max_length=15)
    SEX_CHOICES =(
        ('男', 'male'),
        ('女', 'female'),
    )
    sex = models.CharField(max_length=2, choices=SEX_CHOICES)
    credit = models.IntegerField()


