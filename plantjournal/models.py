from django.db import models
from django.urls import reverse


class Light(models.Model):
    light_id = models.AutoField(primary_key=True)
    light_type = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.light_type

    def get_absolute_url(self):
        return reverse('plantjournal_light_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('plantjournal_light_update_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['light_type']


class Soil(models.Model):
    soil_id = models.AutoField(primary_key=True)
    soil_type = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.soil_type

    def get_absolute_url(self):
        return reverse('plantjournal_soil_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('plantjournal_soil_update_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['soil_type']


class Humidity(models.Model):
    humidity_id = models.AutoField(primary_key=True)
    humidity_level = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.humidity_level

    def get_absolute_url(self):
        return reverse('plantjournal_humidity_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('plantjournal_humidity_update_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['humidity_level']
        verbose_name_plural = 'humidities'


class Water(models.Model):
    water_id = models.AutoField(primary_key=True)
    water_freq = models.CharField(max_length=45)
    water_type = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        if self.water_type == '':
            return '%s' % self.water_freq
        else:
            return '%s (%s)' % (self.water_freq, self.water_type)

    def get_absolute_url(self):
        return reverse('plantjournal_water_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('plantjournal_water_update_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['water_freq', 'water_type']
        unique_together = (('water_freq', 'water_type'),)


class Fertilizer(models.Model):
    fertilizer_id = models.AutoField(primary_key=True)
    fertilizer_freq = models.CharField(max_length=45)
    fertilizer_type = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        if self.fertilizer_type == '':
            return '%s' % self.fertilizer_freq
        else:
            return '%s (%s)' % (self.fertilizer_freq, self.fertilizer_type)

    def get_absolute_url(self):
        return reverse('plantjournal_fertilizer_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('plantjournal_fertilizer_update_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['fertilizer_freq', 'fertilizer_type']
        unique_together = (('fertilizer_freq', 'fertilizer_type'),)


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.location_name

    def get_absolute_url(self):
        return reverse('plantjournal_location_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('plantjournal_location_update_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['location_name']


class Toxicity(models.Model):
    toxicity_id = models.AutoField(primary_key=True)
    toxicity_type = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.toxicity_type

    def get_absolute_url(self):
        return reverse('plantjournal_toxicity_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('plantjournal_toxicity_update_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['toxicity_type']
        verbose_name_plural = 'toxicities'


class Flower(models.Model):
    flower_id = models.AutoField(primary_key=True)
    flower_type = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.flower_type

    def get_absolute_url(self):
        return reverse('plantjournal_flower_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('plantjournal_flower_update_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['flower_type']


class Plant(models.Model):
    plant_id = models.AutoField(primary_key=True)
    plant_name = models.CharField(max_length=45)
    plant_number = models.CharField(max_length=45, blank=True, default='')
    plant_nickname = models.CharField(max_length=45, blank=True, default='')
    plant_latin_name = models.CharField(max_length=100, blank=True, default='')
    plant_description = models.TextField(blank=True, default='')
    light = models.ForeignKey(Light, related_name='plants', on_delete=models.PROTECT, blank=True, null=True, default='')
    soil = models.ForeignKey(Soil, related_name='plants', on_delete=models.PROTECT, blank=True, null=True, default='')
    humidity = models.ForeignKey(Humidity, related_name='plants', on_delete=models.PROTECT, blank=True, null=True,
                                 default='')
    water = models.ForeignKey(Water, related_name='plants', on_delete=models.PROTECT, blank=True, null=True, default='')
    fertilizer = models.ForeignKey(Fertilizer, related_name='plants', on_delete=models.PROTECT, blank=True, null=True,
                                   default='')
    toxicity = models.ForeignKey(Toxicity, related_name='plants', on_delete=models.PROTECT, blank=True, null=True,
                                 default='')
    location = models.ForeignKey(Location, related_name='plants', on_delete=models.PROTECT, blank=True, null=True,
                                 default='')
    flower = models.ForeignKey(Flower, related_name='plants', on_delete=models.PROTECT, blank=True, null=True,
                               default='')

    def __str__(self):
        if self.plant_number == '':
            if self.plant_nickname == '':
                return '%s' % self.plant_name
            else:
                return '%s (%s)' % (self.plant_name, self.plant_nickname)
        else:
            if self.plant_nickname == '':
                return '%s %s' % (self.plant_name, self.plant_number)
            else:
                return '%s %s (%s)' % (self.plant_name, self.plant_number, self.plant_nickname)

    def get_absolute_url(self):
        return reverse('plantjournal_plant_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('plantjournal_plant_update_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['plant_name', 'plant_number', 'plant_nickname']
        unique_together = (('plant_name', 'plant_number', 'plant_nickname'),)


class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    note_date = models.DateField()
    note_name = models.CharField(max_length=45)
    note_body = models.TextField()
    plant = models.ForeignKey(Plant, related_name='notes', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.note_name, self.note_date)

    def get_absolute_url(self):
        return reverse('plantjournal_note_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('plantjournal_note_update_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-note_date', 'note_name']
        unique_together = (('note_date', 'note_name'),)


class GrowthType(models.Model):
    growth_type_id = models.AutoField(primary_key=True)
    growth_type_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.growth_type_name

    def get_absolute_url(self):
        return reverse('plantjournal_growth_type_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('plantjournal_growth_type_update_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['growth_type_name']


class GrowthInstance(models.Model):
    growth_instance_id = models.AutoField(primary_key=True)
    growth_instance_date = models.DateField()
    plant = models.ForeignKey(Plant, related_name='growth_instances', on_delete=models.PROTECT)
    growth_type = models.ForeignKey(GrowthType, related_name='growth_instances', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s (%s)' % (self.plant, self.growth_type, self.growth_instance_date)

    def get_absolute_url(self):
        return reverse('plantjournal_growth_instance_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('plantjournal_growth_instance_update_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-growth_instance_date', 'plant', 'growth_type']
        unique_together = (('plant', 'growth_type', 'growth_instance_date'),)
