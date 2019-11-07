from django.db import models


class A(models.Model):
    name = models.CharField(
        unique=True, max_length=100, null=False, blank=False,
    )


class B (models.Model):
    a = models.ForeignKey(
        A, on_delete=models.CASCADE, null=True, blank=True,
    )
    text = models.TextField()
    flag = models.BooleanField()

