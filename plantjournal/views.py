from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader

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


def light_list_view(request):
    light_list = Light.objects.all()
    # light_list = Light.objects.none()
    template = loader.get_template(
        'plantjournal/light_list.html')
    context = {'light_list': light_list}
    output = template.render(context)
    return HttpResponse(output)


def soil_list_view(request):
    soil_list = Soil.objects.all()
    # soil_list = Soil.objects.none()
    template = loader.get_template(
        'plantjournal/soil_list.html')
    context = {'soil_list': soil_list}
    output = template.render(context)
    return HttpResponse(output)


def humidity_list_view(request):
    humidity_list = Humidity.objects.all()
    # humidity_list = Humidity.objects.none()
    template = loader.get_template(
        'plantjournal/humidity_list.html')
    context = {'humidity_list': humidity_list}
    output = template.render(context)
    return HttpResponse(output)


def water_list_view(request):
    water_list = Water.objects.all()
    # water_list = Water.objects.none()
    template = loader.get_template(
        'plantjournal/water_list.html')
    context = {'water_list': water_list}
    output = template.render(context)
    return HttpResponse(output)


def fertilizer_list_view(request):
    fertilizer_list = Fertilizer.objects.all()
    # fertilizer_list = Fertilizer.objects.none()
    template = loader.get_template(
        'plantjournal/fertilizer_list.html')
    context = {'fertilizer_list': fertilizer_list}
    output = template.render(context)
    return HttpResponse(output)


def toxicity_list_view(request):
    toxicity_list = Toxicity.objects.all()
    # toxicity_list = Toxicity.objects.none()
    template = loader.get_template(
        'plantjournal/toxicity_list.html')
    context = {'toxicity_list': toxicity_list}
    output = template.render(context)
    return HttpResponse(output)


def location_list_view(request):
    location_list = Location.objects.all()
    # location_list = Location.objects.none()
    template = loader.get_template(
        'plantjournal/location_list.html')
    context = {'location_list': location_list}
    output = template.render(context)
    return HttpResponse(output)


def flower_list_view(request):
    flower_list = Flower.objects.all()
    # flower_list = Flower.objects.none()
    template = loader.get_template(
        'plantjournal/flower_list.html')
    context = {'flower_list': flower_list}
    output = template.render(context)
    return HttpResponse(output)


def plant_list_view(request):
    plant_list = Plant.objects.all()
    # plant_list = Plant.objects.none()
    template = loader.get_template(
        'plantjournal/plant_list.html')
    context = {'plant_list': plant_list}
    output = template.render(context)
    return HttpResponse(output)


def note_list_view(request):
    note_list = Note.objects.all()
    # note_list = Note.objects.none()
    template = loader.get_template(
        'plantjournal/note_list.html')
    context = {'note_list': note_list}
    output = template.render(context)
    return HttpResponse(output)


def growth_type_list_view(request):
    growth_type_list = GrowthType.objects.all()
    # growth_type_list = GrowthType.objects.none()
    template = loader.get_template(
        'plantjournal/growth_type_list.html')
    context = {'growth_type_list': growth_type_list}
    output = template.render(context)
    return HttpResponse(output)


def growth_instance_list_view(request):
    growth_instance_list = GrowthInstance.objects.all()
    # growth_instance_list = GrowthInstance.objects.none()
    template = loader.get_template(
        'plantjournal/growth_instance_list.html')
    context = {'growth_instance_list': growth_instance_list}
    output = template.render(context)
    return HttpResponse(output)
