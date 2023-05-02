from django.db import models

class Post(models.Model):
    
    item_name = models.CharField(max_length=100)
    amount = models.IntegerField()

    weight = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)