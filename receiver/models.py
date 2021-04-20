from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class Res_type(models.Model):
    resource_name = models.CharField(max_length=50)
    more_info = models.CharField(max_length=200)

    def __str__(self):
        return self.resource_name


state_choices = (("Andhra Pradesh", "Andhra Pradesh"), ("Arunachal Pradesh ", "Arunachal Pradesh "), ("Assam", "Assam"), ("Bihar", "Bihar"), ("Chhattisgarh", "Chhattisgarh"), ("Goa", "Goa"), ("Gujarat", "Gujarat"), ("Haryana", "Haryana"), ("Himachal Pradesh", "Himachal Pradesh"), ("Jammu and Kashmir ", "Jammu and Kashmir "), ("Jharkhand", "Jharkhand"), ("Karnataka", "Karnataka"), ("Kerala", "Kerala"), ("Madhya Pradesh", "Madhya Pradesh"), ("Maharashtra", "Maharashtra"), ("Manipur", "Manipur"), ("Meghalaya", "Meghalaya"), ("Mizoram", "Mizoram"), ("Nagaland", "Nagaland"), ("Odisha", "Odisha"),
                 ("Punjab", "Punjab"), ("Rajasthan", "Rajasthan"), ("Sikkim", "Sikkim"), ("Tamil Nadu", "Tamil Nadu"), ("Telangana", "Telangana"), ("Tripura", "Tripura"), ("Uttar Pradesh", "Uttar Pradesh"), ("Uttarakhand", "Uttarakhand"), ("West Bengal", "West Bengal"), ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"), ("Chandigarh", "Chandigarh"), ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"), ("Daman and Diu", "Daman and Diu"), ("Lakshadweep", "Lakshadweep"), ("National Capital Territory of Delhi", "National Capital Territory of Delhi"), ("Puducherry", "Puducherry"))


class Resource(models.Model):
    contact_name = models.CharField(default='', max_length=200)
    email_id = models.CharField(default='', max_length=200)
    phone = models.CharField(default='', max_length=200)

    #qty: models.CharField(default='', max_length=200)
    state = models.CharField(choices=state_choices,
                             max_length=255, null=True, blank=True)
    city = models.CharField(default='', max_length=200)
    # resource_name = models.ForeignKey(
    #     Res_type, default='del', verbose_name="Category", on_delete=models.SET_DEFAULT)
    description = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now, auto_created=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.contact_name + self.resource_name


class Needy(models.Model):
    name = models.CharField(max_length=200)
    email_id = models.CharField(default='', max_length=200)
    phone = models.CharField(default='', max_length=200)
    state = models.CharField(choices=state_choices,
                             max_length=255, null=True, blank=True)
    city = models.CharField(default='', max_length=200)
    # resource_name = models.ForeignKey(
    #     Res_type, default='del', verbose_name="Category", on_delete=models.SET_DEFAULT)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now, auto_created=True)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return (f"{self.pub_date >= timezone.now() - datetime.timedelta(days=1)}")
