from django.db import models

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)