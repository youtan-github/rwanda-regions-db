from django.db import models
from .utilities import generate_unique_code
# Create your models here.


class Place(models.Model):
    code = models.CharField(max_length=11, unique=True)
    name = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        self.code = generate_unique_code()
        super(Place, self).save(*args, **kwargs)


class Province(Place):
    pass


class District(models.Model):
    related_province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)


class Sector(models.Model):
    related_district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)


class Cell(models.Model):
    related_sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True)


class Village(models.Model):
    related_cell = models.ForeignKey(Cell, on_delete=models.SET_NULL, null=True)
