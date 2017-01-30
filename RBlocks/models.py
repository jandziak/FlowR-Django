from django.db import models


class Box(models.Model):
    name = models.CharField(max_length=100)
    type_id = models.CharField(max_length=100)

    def __str__(self):
        return self.type_id


class Specification(models.Model):
    param = models.CharField(max_length=100)
    type = models.ForeignKey(Box, on_delete=models.CASCADE)
    value = models.CharField(max_length=5000)

    def __str__(self):
        return self.value
