from django.db import models


# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()

    def __str__(self):
        return f'{str(self.id)}: {self.title}'
