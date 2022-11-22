from adaptor.model import CsvModel
from adaptor.fields import CharField,FloatField,IntegerField
from django.db import models
from django.contrib.auth.models import User

class Moviedetails(models.Model):
  movie_title = models.CharField(max_length=255)
  rating=models.FloatField()
  year =models.IntegerField()
  rank =models.IntegerField()
  star_cast=models.CharField(max_length=255)
  def __str__(self):
        return f"Item ID: {self.year} | Title: {self.movie_title}"

class Watchlist(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   item = models.ManyToManyField(Moviedetails)
   def __str__(self):
       return f"{self.user}'s WatchList"

#   class Meta:
#     delimiter=","


# Create your models here.
