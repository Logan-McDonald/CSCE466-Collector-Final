# from django.db import models

# Create your models here.
# class Message(models.Model):
#     sender = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='sent_messages')
#     receiver = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='received_messages')
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.conf import settings

class Message(models.Model):
    sender   = models.ForeignKey(
                   settings.AUTH_USER_MODEL,
                   related_name='sent_messages',
                   on_delete=models.CASCADE
               )
    receiver = models.ForeignKey(
                   settings.AUTH_USER_MODEL,
                   related_name='received_messages',
                   on_delete=models.CASCADE
               )
    content  = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
