from django.db import models

# Create your models here.
class MovieInfo(models.Model):
    Movie=models.CharField(max_length=100)
    Release_Year=models.DateTimeField(auto_now_add= True)
    Actor=models.CharField(max_length=50, help_text="add Hero / Actress name")

class LoginForm(models.Model):
    name=models.CharField(max_length=100)


class Review(models.Model):
    RATING_RANGE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
        )
    rating = models.IntegerField(choices=RATING_RANGE,)
