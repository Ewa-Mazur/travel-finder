from django.db import models

class Continent(models.Model):
    # relation many to many 
    name = models.CharField(max_length=80)
    
    def __str__(self):
        return f"{self.name}"
    

class Destination(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    continent = models.ManyToManyField(Continent,)
    latitude = models.FloatField()
    longitude = models.FloatField()
    avg_year_temp = models.IntegerField()
    is_beach = models.BooleanField()
    are_mountains = models.BooleanField()
    top_attractions = models.CharField(max_length=500)
    hotel_price = models.IntegerField()
    description = models.TextField()
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)

    def __str__(self):
        return f"{self.city}, {self.country}"


