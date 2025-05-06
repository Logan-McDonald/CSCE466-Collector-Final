from django.db import models

# Create your models here.
class Collection(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Item(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='items')  # Add related_name here
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)

    def __str__(self):
        return self.name
