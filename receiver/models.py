from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class Res_type(models.Model):
    resource_name = models.CharField(max_length=50)
    more_info = models.CharField(
        default='', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.resource_name


class State(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(
        State, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Resource(models.Model):
    contact_name = models.CharField(default='', max_length=200)
    email_id = models.CharField(default='', max_length=200)
    web_site = models.CharField(default='', max_length=200)
    phone = models.CharField(default='', max_length=200)
    #qty: models.CharField(default='', max_length=200)
    state = models.ForeignKey(
        State, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, blank=True, null=True)
    resource_name = models.ForeignKey(
        Res_type, verbose_name="resc_type", on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=200, blank=True, null=True)

    verified = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now, auto_created=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.contact_name


class Needy(models.Model):
    name = models.CharField(max_length=200)
    email_id = models.CharField(default='', max_length=200)
    phone = models.CharField(default='', max_length=200)
    state = models.ForeignKey(
        State, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, blank=True, null=True)
    resource_name = models.ForeignKey(
        Res_type, default='del', verbose_name="resc_type", on_delete=models.SET_DEFAULT)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now, auto_created=True)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return (f"{self.pub_date >= timezone.now() - datetime.timedelta(days=1)}")


class Feedback(models.Model):
    phone = models.CharField(default='', max_length=200)
    suggest = models.CharField(max_length=500)
    any_misconduct = models.CharField(max_length=500)

    def __str__(self):
        return self.phone
