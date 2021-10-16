from django.db import models


class Activity(models.Model):
    type = models.CharField(max_length=255)
    score = models.IntegerField()

    class Categories(models.TextChoices):
        WANT = 'V',
        MUST = 'M',
        DISPOSABLE = 'K'

    category = models.CharField(
        max_length=1,
        choices=Categories.choices,
        default=Categories.WANT
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.IntegerField()