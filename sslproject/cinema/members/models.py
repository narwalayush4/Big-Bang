from adaptor.model import CsvModel
from adaptor.fields import CharField,FloatField,IntegerField
from django.db import models
from django.contrib.auth.models import User

class Moviedetails(models.Model):
  movie_title = models.CharField(max_length=255)
  movie_id = models.CharField(max_length=255,null=True)
  poster= models.URLField(null=True)
  year =models.IntegerField(null=True,)
  release=models.CharField(max_length=255,null=True,)
  star_cast=models.CharField(max_length=255)
  rating1=models.FloatField(null=True,)
  review1=models.CharField(max_length=255,null=True,)
  rating2=models.FloatField(null=True,)
  review2=models.CharField(max_length=255,null=True,)
  rating3=models.FloatField(null=True,)
  review3=models.CharField(max_length=255,null=True,)
  rating4=models.FloatField(null=True,)
  review4=models.CharField(max_length=255,null=True,)
  genre=models.CharField(max_length=255,null=True,)
  plot=models.CharField(max_length=255,null=True,)
  duration =models.IntegerField(null=True,)
  rating =models.FloatField(null=True,)
  platform=models.CharField(max_length=255,null=True,)
  Language=models.CharField(max_length=255,null=True,)
  sim_mov1=models.CharField(max_length=255,null=True,)
  sim_mov2=models.CharField(max_length=255,null=True,)
  sim_mov3=models.CharField(max_length=255,null=True,)
  sim_mov4=models.CharField(max_length=255,null=True,)
  sim_pos1=models.URLField(null=True)
  sim_pos2=models.URLField(null=True)
  sim_pos3=models.URLField(null=True)
  sim_pos4=models.URLField(null=True)
 
  def __str__(self):
        return f"Movie_poster: {self.poster} | Title: {self.movie_title}"

class Watchlist(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   item = models.ManyToManyField(Moviedetails)
   def __str__(self):
       return f"{self.user}'s WatchList"

class Towatch(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   item = models.ManyToManyField(Moviedetails)
   def __str__(self):
       return f"{self.user}'s Towatch"

class Liked(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   item = models.ManyToManyField(Moviedetails)
   def __str__(self):
       return f"{self.user}'s Liked"

#   class Meta:
#     delimiter=","


# Create your models here.
