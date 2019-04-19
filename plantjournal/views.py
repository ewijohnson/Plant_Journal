from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader
from django.views import View

from .models import (
    Light,
    Soil,
    Humidity,
    Water,
    Fertilizer,
    Toxicity,
    Location,
    Flower,
    Plant,
    Note,
    GrowthType,
    GrowthInstance,
)


class LightList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/light_list.html',
            {'light_list': Light.objects.all()}
        )


class SoilList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/soil_list.html',
            {'soil_list': Soil.objects.all()}
        )


class HumidityList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/humidity_list.html',
            {'humidity_list': Humidity.objects.all()}
        )


class WaterList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/water_list.html',
            {'water_list': Water.objects.all()}
        )


class FertilizerList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/fertilizer_list.html',
            {'fertilizer_list': Fertilizer.objects.all()}
        )


class ToxicityList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/toxicity_list.html',
            {'toxicity_list': Toxicity.objects.all()}
        )


class LocationList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/location_list.html',
            {'location_list': Location.objects.all()}
        )


class FlowerList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/flower_list.html',
            {'flower_list': Flower.objects.all()}
        )


class PlantList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/plant_list.html',
            {'plant_list': Plant.objects.all()}
        )


class NoteList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/note_list.html',
            {'note_list': Note.objects.all()}
        )


class GrowthTypeList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/growth_type_list.html',
            {'growth_type_list': GrowthType.objects.all()}
        )


class GrowthInstanceList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/growth_instance_list.html',
            {'growth_instance_list': GrowthInstance.objects.all()}
        )
