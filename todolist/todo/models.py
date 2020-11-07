from django.db import models

# Create your models here.
class todom(models.Model):
    content=models.TextField()

    def __self__(self):
        return self.content