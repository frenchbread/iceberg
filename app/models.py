from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=100)
    start_day = models.DateField()
    start_time = models.TimeField(blank=True, default='09:00:00')
    description = models.TextField(max_length=300, blank=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name