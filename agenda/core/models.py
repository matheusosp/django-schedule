from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.

class event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    data_event = models.DateTimeField(verbose_name="Data of Event")
    data_create = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    local = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        db_table = 'event'

    def __str__(self):
       return self.title     

    def get_data_event(self):
        return self.data_event.strftime('%d/%m/%Y %H:%M Hours')   

    def get_data_input(self):
        return self.data_event.strftime('%Y-%m-%dT%H:%M')    

    def get_delayed_event(self):
        if self.data_event < datetime.now():
            return True
        elif self.data_event-timedelta(hours=1) < datetime.now() and self.data_event > datetime.now():
            return False
        return   