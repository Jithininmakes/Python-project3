from django.db import models
from pyexpat import model


# Create your models here.

class table (models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name









