from django.db import models


class Light(models.Model):
    light_id = models.AutoField(primary_key=True)
    light_type = models.CharField(max_length=45, unique=True)


class Soil(models.Model):
    soil_id = models.AutoField(primary_key=True)
    soil_type = models.CharField(max_length=45, unique=True)


class Humidity(models.Model):
    humidity_id = models.AutoField(primary_key=True)
    humidity_level = models.CharField(max_length=45, unique=True)


class Water(models.Model):
    water_id = models.AutoField(primary_key=True)
    water_freq = models.CharField(max_length=45)
    water_type = models.CharField(max_length=45, blank=True, default='')


class Fertilizer(models.Model):
    fertilizer_id = models.AutoField(primary_key=True)
    fertilizer_freq = models.CharField(max_length=45)
    fertilizer_type = models.CharField(max_length=45, blank=True, default='')


class Toxicity(models.Model):
    toxicity_id = models.AutoField(primary_key=True)
    toxicity_description = models.TextField()


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=45, unique=True)


class Flower(models.Model):
    flower_id = models.AutoField(primary_key=True)
    flower_type = models.CharField(max_length=45, unique=True)
    flower_date_last = models.DateField(blank=True, default='')


class Plant(models.Model):
    plant_id = models.AutoField(primary_key=True)
    plant_name = models.CharField(max_length=45)
    plant_number = models.CharField(max_length=45, blank=True, default='')
    plant_latin_name = models.CharField(max_length=100, blank=True, default='')
    plant_nickname = models.CharField(max_length=45, blank=True, default='')
    plant_description = models.TextField(blank=True, default='')
    light = models.ForeignKey(Light, related_name='plants', on_delete=models.PROTECT, blank=True, default='')
    soil = models.ForeignKey(Soil, related_name='plants', on_delete=models.PROTECT, blank=True, default='')
    humidity = models.ForeignKey(Humidity, related_name='plants', on_delete=models.PROTECT, blank=True, default='')
    water = models.ForeignKey(Water, related_name='plants', on_delete=models.PROTECT, blank=True, default='')
    fertilizer = models.ForeignKey(Fertilizer, related_name='plants', on_delete=models.PROTECT, blank=True, default='')
    toxicity = models.ForeignKey(Toxicity, related_name='plants', on_delete=models.PROTECT, blank=True, default='')
    location = models.ForeignKey(Location, related_name='plants', on_delete=models.PROTECT, blank=True, default='')
    flower = models.ForeignKey(Flower, related_name='plants', on_delete=models.PROTECT, blank=True, default='')


class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    note_date = models.DateField()
    note_name = models.CharField(max_length=45, unique=True)
    note_body = models.TextField()
    plant = models.ForeignKey(Plant, related_name='notes', on_delete=models.PROTECT)


class GrowthType(models.Model):
    growth_type_id = models.AutoField(primary_key=True)
    growth_type_name = models.CharField(max_length=45)


class GrowthInstance(models.Model):
    growth_instance_id = models.AutoField(primary_key=True)
    plant = models.ForeignKey(Plant, related_name='growth_instances', on_delete=models.PROTECT)
    growth_type = models.ForeignKey(GrowthType, related_name='growth_instances', on_delete=models.PROTECT)
