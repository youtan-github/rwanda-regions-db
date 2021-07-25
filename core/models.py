from django.db import models
from django.utils.crypto import get_random_string
# Create your models here.


class Place(models.Model):
    code = models.CharField(max_length=11, unique=True)
    name = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=250)

    def generate_unique_code(self):
        code = get_random_string(7)
        object_test = Place.objects.filter(code=code).exists()
        while object_test:
            code = get_random_string(9)
            object_test = Place.objects.filter(code=code).exists()
        self.code = 'RW-' + code

    def save(self, *args, **kwargs):
        self.generate_unique_code()
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
