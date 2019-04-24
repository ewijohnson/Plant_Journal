from django.shortcuts import render, get_object_or_404
from django.views import View

from plantjournal.forms import LightForm, SoilForm, HumidityForm, WaterForm, FertilizerForm, LocationForm, \
    ToxicityForm, FlowerForm, PlantForm, NoteForm, GrowthTypeForm, GrowthInstanceForm
from plantjournal.utils import ObjectCreateMixin
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


class LightDetail(View):

    def get(self, request, pk):
        light = get_object_or_404(
            Light,
            pk=pk
        )
        plant_list = light.plants.all()
        return render(
            request,
            'plantjournal/light_detail.html',
            {'light': light, 'plant_list': plant_list}
        )


class LightCreate(ObjectCreateMixin, View):
    form_class = LightForm
    template_name = 'plantjournal/light_form.html'


class SoilList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/soil_list.html',
            {'soil_list': Soil.objects.all()}
        )


class SoilDetail(View):

    def get(self, request, pk):
        soil = get_object_or_404(
            Soil,
            pk=pk
        )
        plant_list = soil.plants.all()
        return render(
            request,
            'plantjournal/soil_detail.html',
            {'soil': soil, 'plant_list': plant_list}
        )


class SoilCreate(ObjectCreateMixin, View):
    form_class = SoilForm
    template_name = 'plantjournal/soil_form.html'


class HumidityList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/humidity_list.html',
            {'humidity_list': Humidity.objects.all()}
        )


class HumidityDetail(View):

    def get(self, request, pk):
        humidity = get_object_or_404(
            Humidity,
            pk=pk
        )
        plant_list = humidity.plants.all()
        return render(
            request,
            'plantjournal/humidity_detail.html',
            {'humidity': humidity, 'plant_list': plant_list}
        )


class HumidityCreate(ObjectCreateMixin, View):
    form_class = HumidityForm
    template_name = 'plantjournal/humidity_form.html'


class WaterList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/water_list.html',
            {'water_list': Water.objects.all()}
        )


class WaterDetail(View):

    def get(self, request, pk):
        water = get_object_or_404(
            Water,
            pk=pk
        )
        plant_list = water.plants.all()
        return render(
            request,
            'plantjournal/water_detail.html',
            {'water': water, 'plant_list': plant_list}
        )


class WaterCreate(ObjectCreateMixin, View):
    form_class = WaterForm
    template_name = 'plantjournal/water_form.html'


class FertilizerList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/fertilizer_list.html',
            {'fertilizer_list': Fertilizer.objects.all()}
        )


class FertilizerDetail(View):

    def get(self, request, pk):
        fertilizer = get_object_or_404(
            Fertilizer,
            pk=pk
        )
        plant_list = fertilizer.plants.all()
        return render(
            request,
            'plantjournal/fertilizer_detail.html',
            {'fertilizer': fertilizer, 'plant_list': plant_list}
        )


class FertilizerCreate(ObjectCreateMixin, View):
    form_class = FertilizerForm
    template_name = 'plantjournal/fertilizer_form.html'


class LocationList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/location_list.html',
            {'location_list': Location.objects.all()}
        )


class LocationDetail(View):

    def get(self, request, pk):
        location = get_object_or_404(
            Location,
            pk=pk
        )
        plant_list = location.plants.all()
        return render(
            request,
            'plantjournal/location_detail.html',
            {'location': location, 'plant_list': plant_list}
        )


class LocationCreate(ObjectCreateMixin, View):
    form_class = LocationForm
    template_name = 'plantjournal/location_form.html'


class ToxicityList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/toxicity_list.html',
            {'toxicity_list': Toxicity.objects.all()}
        )


class ToxicityDetail(View):

    def get(self, request, pk):
        toxicity = get_object_or_404(
            Toxicity,
            pk=pk
        )
        plant_list = toxicity.plants.all()
        return render(
            request,
            'plantjournal/toxicity_detail.html',
            {'toxicity': toxicity, 'plant_list': plant_list}
        )


class ToxicityCreate(ObjectCreateMixin, View):
    form_class = ToxicityForm
    template_name = 'plantjournal/toxicity_form.html'


class FlowerList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/flower_list.html',
            {'flower_list': Flower.objects.all()}
        )


class FlowerDetail(View):

    def get(self, request, pk):
        flower = get_object_or_404(
            Flower,
            pk=pk
        )
        plant_list = flower.plants.all()
        return render(
            request,
            'plantjournal/flower_detail.html',
            {'flower': flower, 'plant_list': plant_list}
        )


class FlowerCreate(ObjectCreateMixin, View):
    form_class = FlowerForm
    template_name = 'plantjournal/flower_form.html'


class PlantList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/plant_list.html',
            {'plant_list': Plant.objects.all()}
        )


class PlantDetail(View):

    def get(self, request, pk):
        plant = get_object_or_404(
            Plant,
            pk=pk
        )
        light = plant.light
        soil = plant.soil
        humidity = plant.humidity
        water = plant.water
        fertilizer = plant.fertilizer
        location = plant.location
        toxicity = plant.toxicity
        flower = plant.flower
        growth_instance_list = plant.growth_instances.all()
        note_list = plant.notes.all()
        return render(
            request,
            'plantjournal/plant_detail.html',
            {'plant': plant,
             'light': light,
             'soil': soil,
             'humidity': humidity,
             'water': water,
             'fertilizer': fertilizer,
             'location': location,
             'toxicity': toxicity,
             'flower': flower,
             'growth_instance_list': growth_instance_list,
             'note_list': note_list}
        )


class PlantCreate(ObjectCreateMixin, View):
    form_class = PlantForm
    template_name = 'plantjournal/plant_form.html'


class NoteList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/note_list.html',
            {'note_list': Note.objects.all()}
        )


class NoteDetail(View):

    def get(self, request, pk):
        note = get_object_or_404(
            Note,
            pk=pk
        )
        plant = note.plant
        return render(
            request,
            'plantjournal/note_detail.html',
            {'note': note, 'plant': plant}
        )


class NoteCreate(ObjectCreateMixin, View):
    form_class = NoteForm
    template_name = 'plantjournal/note_form.html'


class GrowthTypeList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/growth_type_list.html',
            {'growth_type_list': GrowthType.objects.all()}
        )


class GrowthTypeDetail(View):

    def get(self, request, pk):
        growth_type = get_object_or_404(
            GrowthType,
            pk=pk
        )
        growth_instance_list = growth_type.growth_instances.all()
        return render(
            request,
            'plantjournal/growth_type_detail.html',
            {'growth_type': growth_type, 'growth_instance_list': growth_instance_list}
        )


class GrowthTypeCreate(ObjectCreateMixin, View):
    form_class = GrowthTypeForm
    template_name = 'plantjournal/growth_type_form.html'


class GrowthInstanceList(View):

    def get(self, request):
        return render(
            request,
            'plantjournal/growth_instance_list.html',
            {'growth_instance_list': GrowthInstance.objects.all()}
        )


class GrowthInstanceDetail(View):

    def get(self, request, pk):
        growth_instance = get_object_or_404(
            GrowthInstance,
            pk=pk
        )
        plant = growth_instance.plant
        growth_type = growth_instance.growth_type
        return render(
            request,
            'plantjournal/growth_instance_detail.html',
            {'growth_instance': growth_instance,
             'plant': plant,
             'growth_type': growth_type}
        )


class GrowthInstanceCreate(ObjectCreateMixin, View):
    form_class = GrowthInstanceForm
    template_name = 'plantjournal/growth_instance_form.html'
