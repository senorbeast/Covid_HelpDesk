from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class Needy(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    request = models.CharField(default='', max_length=200)
    state_choice = models.CharField(default='', max_length=200)

    def __str__(self):
        return (f"{self.name}")

    def was_published_recently(self):
        return (f"{self.pub_date >= timezone.now() - datetime.timedelta(days=1)}")
