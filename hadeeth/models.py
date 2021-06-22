from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Hadeeth(models.Model):
    content = models.TextField()
    book = models.CharField(max_length=256)
    narrator = models.CharField(max_length=64)
    uploaded_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.content
