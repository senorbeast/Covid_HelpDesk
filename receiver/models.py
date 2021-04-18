from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class Needy(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name, self.pub_date

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Request(models.Model):
    request = models.ForeignKey(Needy, on_delete=models.CASCADE)
    state_choice = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)

    def __str__(self):
        return self.request, self.state_choice
