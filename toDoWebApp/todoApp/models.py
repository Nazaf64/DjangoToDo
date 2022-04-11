import uuid
from django.db import models

# Create your models here.

class TodoList(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    # task = models.TextField()
    task = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task