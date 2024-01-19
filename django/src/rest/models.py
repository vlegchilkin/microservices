from django.db import models


class CustomModel(models.Model):
    my_field = models.CharField(max_length=255)
