from django.db import models

# Create your models here.
class Page(models.Model):
    number = models.IntegerField(max_length=10, unique=True, null=False, blank=False)
    android = models.URLField(max_length=200, null=True, blank=True)
    ios = models.URLField(max_length=200, null=True, blank=True)
    other = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.number