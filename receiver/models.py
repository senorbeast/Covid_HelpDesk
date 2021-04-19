from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class Resource(models.Model):
    resource_name = models.CharField(default='', max_length=200)
    #qty: models.CharField(default='', max_length=200)
    state = models.CharField(default='', max_length=200)
    city = models.CharField(default='', max_length=200)
    contact_name = models.CharField(default='', max_length=200)
    email_id = models.CharField(default='', max_length=200)
    phone = models.CharField(default='', max_length=200)
    last_updated = models.DateField('last updated')


class Needy(models.Model):
    name = models.CharField(max_length=200)
    email_id = models.CharField(default='', max_length=200)
    phone = models.CharField(default='', max_length=200)
    req = models.CharField(default='', max_length=200)
    state = models.CharField(default='', max_length=200)
    city = models.CharField(default='', max_length=200)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return (f"{self.pub_date >= timezone.now() - datetime.timedelta(days=1)}")
