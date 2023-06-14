from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models


class Test(models.Model):
    login = models.CharField(max_length=10, validators=[MinLengthValidator(10)], unique=True)


class IQ(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=10, validators=[MinValueValidator(0), MaxValueValidator(50)])
    time = models.DateTimeField(auto_now_add=True)


class EQ(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    letters = models.CharField(max_length=5, validators=[MinLengthValidator(5)])
    time = models.DateTimeField(auto_now_add=True)
