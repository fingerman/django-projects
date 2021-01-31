from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
