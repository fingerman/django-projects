from django.db import models


class Animal(models.Model):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    PRIORITY_CHOICE = (
        (LOW, 'low'),
        (MEDIUM, 'medium'),
        (HIGH, 'high'),
    )

    name = models.CharField(max_length=20)
    image_url = models.URLField()
    description = models.TextField(max_length=250)
    priority = models.CharField(max_length=8, choices=PRIORITY_CHOICE, default=LOW)
    is_cured = models.BooleanField(default=False)
