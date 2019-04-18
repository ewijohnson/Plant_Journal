from django.contrib import admin
from .models import Light, Soil, Humidity, Water, Fertilizer, Toxicity, Location, Flower, \
    Plant, Note, GrowthType, GrowthInstance


admin.site.register(Light)
admin.site.register(Soil)
admin.site.register(Humidity)
admin.site.register(Water)
admin.site.register(Fertilizer)
admin.site.register(Toxicity)
admin.site.register(Location)
admin.site.register(Flower)
admin.site.register(Plant)
admin.site.register(Note)
admin.site.register(GrowthType)
admin.site.register(GrowthInstance)
