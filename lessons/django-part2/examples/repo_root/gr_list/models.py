from django.db import models

class Post(models.Model):
    
    item_name = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)

    weight = models.IntegerField(default=None)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self): #__str__ for python3
        return self.item_name