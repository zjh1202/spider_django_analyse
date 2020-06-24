from django.test import TestCase

# Create your tests here.
from analysis import models


def analysis():
    all = models.Zhipin.objects.all()
    for list in all:
        job = list.job
        print(job)