from __future__ import unicode_literals

from django.db import models


class Messages(models.Model):
    message_id = models.CharField(max_length=255)
    receive_date = models.DateTimeField('date message received')
    set_date = models.DateTimeField('date scheduled for delivery')
    message_body = models.CharField(max_length=255)
    message_email = models.CharField(max_length=255)
