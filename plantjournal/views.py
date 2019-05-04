from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from plantjournal.forms import LightForm, SoilForm, HumidityForm, WaterForm, FertilizerForm, LocationForm, \
    ToxicityForm, FlowerForm, PlantForm, NoteForm, GrowthTypeForm, GrowthInstanceForm
from plantjournal.utils import PageLinksMixin

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


class LightList(ListView):
    model = Light


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


class LightCreate(CreateView):
    form_class = LightForm
    model = Light


class LightUpdate(UpdateView):
    form_class = LightForm
    model = Light
    template_name = 'plantjournal/light_form_update.html'


class LightDelete(View):

    def get(self, request, pk):
        light = self.get_object(pk)
        plants = light.plants.all()
        if plants.count() > 0:
            return render(
                request,
                'plantjournal/light_refuse_delete.html',
                {'light': light,
                 'plants': plants}
            )
        else:
            return render(
                request,
                'plantjournal/light_confirm_delete.html',
                {'light': light}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Light,
            pk=pk
        )

    def post(self, request, pk):
        light = self.get_object(pk)
        light.delete()
        return redirect('plantjournal_light_list_urlpattern')


class SoilList(PageLinksMixin, ListView):
    paginate_by = 20
    model = Soil


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


class SoilCreate(CreateView):
    form_class = SoilForm
    model = Soil


class SoilUpdate(UpdateView):
    form_class = SoilForm
    model = Soil
    template_name = 'plantjournal/soil_form_update.html'


class SoilDelete(View):

    def get(self, request, pk):
        soil = self.get_object(pk)
        plants = soil.plants.all()
        if plants.count() > 0:
            return render(
                request,
                'plantjournal/soil_refuse_delete.html',
                {'soil': soil,
                 'plants': plants}
            )
        else:
            return render(
                request,
                'plantjournal/soil_confirm_delete.html',
                {'soil': soil}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Soil,
            pk=pk
        )

    def post(self, request, pk):
        soil = self.get_object(pk)
        soil.delete()
        return redirect('plantjournal_soil_list_urlpattern')


class HumidityList(ListView):
    model = Humidity


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


class HumidityCreate(CreateView):
    form_class = HumidityForm
    model = Humidity


class HumidityUpdate(UpdateView):
    form_class = HumidityForm
    model = Humidity
    template_name = 'plantjournal/humidity_form_update.html'


class HumidityDelete(View):

    def get(self, request, pk):
        humidity = self.get_object(pk)
        plants = humidity.plants.all()
        if plants.count() > 0:
            return render(
                request,
                'plantjournal/humidity_refuse_delete.html',
                {'humidity': humidity,
                 'plants': plants}
            )
        else:
            return render(
                request,
                'plantjournal/humidity_confirm_delete.html',
                {'humidity': humidity}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Humidity,
            pk=pk
        )

    def post(self, request, pk):
        humidity = self.get_object(pk)
        humidity.delete()
        return redirect('plantjournal_humidity_list_urlpattern')


class WaterList(PageLinksMixin, ListView):
    paginate_by = 20
    model = Water


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


class WaterCreate(CreateView):
    form_class = WaterForm
    model = Water


class WaterUpdate(UpdateView):
    form_class = WaterForm
    model = Water
    template_name = 'plantjournal/water_form_update.html'


class WaterDelete(View):

    def get(self, request, pk):
        water = self.get_object(pk)
        plants = water.plants.all()
        if plants.count() > 0:
            return render(
                request,
                'plantjournal/water_refuse_delete.html',
                {'water': water,
                 'plants': plants}
            )
        else:
            return render(
                request,
                'plantjournal/water_confirm_delete.html',
                {'water': water}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Water,
            pk=pk
        )

    def post(self, request, pk):
        water = self.get_object(pk)
        water.delete()
        return redirect('plantjournal_water_list_urlpattern')


class FertilizerList(PageLinksMixin, ListView):
    paginate_by = 20
    model = Fertilizer


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


class FertilizerCreate(CreateView):
    form_class = FertilizerForm
    model = Fertilizer


class FertilizerUpdate(UpdateView):
    form_class = FertilizerForm
    model = Fertilizer
    template_name = 'plantjournal/fertilizer_form_update.html'


class FertilizerDelete(View):

    def get(self, request, pk):
        fertilizer = self.get_object(pk)
        plants = fertilizer.plants.all()
        if plants.count() > 0:
            return render(
                request,
                'plantjournal/fertilizer_refuse_delete.html',
                {'fertilizer': fertilizer,
                 'plants': plants}
            )
        else:
            return render(
                request,
                'plantjournal/fertilizer_confirm_delete.html',
                {'fertilizer': fertilizer}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Fertilizer,
            pk=pk
        )

    def post(self, request, pk):
        fertilizer = self.get_object(pk)
        fertilizer.delete()
        return redirect('plantjournal_fertilizer_list_urlpattern')


class LocationList(PageLinksMixin, ListView):
    paginate_by = 20
    model = Location


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


class LocationCreate(CreateView):
    form_class = LocationForm
    model = Location


class LocationUpdate(UpdateView):
    form_class = LocationForm
    model = Location
    template_name = 'plantjournal/location_form_update.html'


class LocationDelete(View):

    def get(self, request, pk):
        location = self.get_object(pk)
        plants = location.plants.all()
        if plants.count() > 0:
            return render(
                request,
                'plantjournal/location_refuse_delete.html',
                {'location': location,
                 'plants': plants}
            )
        else:
            return render(
                request,
                'plantjournal/location_confirm_delete.html',
                {'location': location}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Location,
            pk=pk
        )

    def post(self, request, pk):
        location = self.get_object(pk)
        location.delete()
        return redirect('plantjournal_location_list_urlpattern')


class ToxicityList(ListView):
    model = Toxicity


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


class ToxicityCreate(CreateView):
    form_class = ToxicityForm
    model = Toxicity


class ToxicityUpdate(UpdateView):
    form_class = ToxicityForm
    model = Toxicity
    template_name = 'plantjournal/toxicity_form_update.html'


class ToxicityDelete(View):

    def get(self, request, pk):
        toxicity = self.get_object(pk)
        plants = toxicity.plants.all()
        if plants.count() > 0:
            return render(
                request,
                'plantjournal/toxicity_refuse_delete.html',
                {'toxicity': toxicity,
                 'plants': plants}
            )
        else:
            return render(
                request,
                'plantjournal/toxicity_confirm_delete.html',
                {'toxicity': toxicity}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Toxicity,
            pk=pk
        )

    def post(self, request, pk):
        toxicity = self.get_object(pk)
        toxicity.delete()
        return redirect('plantjournal_toxicity_list_urlpattern')


class FlowerList(PageLinksMixin, ListView):
    paginate_by = 20
    model = Flower


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


class FlowerCreate(CreateView):
    form_class = FlowerForm
    model = Flower


class FlowerUpdate(UpdateView):
    form_class = FlowerForm
    model = Flower
    template_name = 'plantjournal/flower_form_update.html'


class FlowerDelete(View):

    def get(self, request, pk):
        flower = self.get_object(pk)
        plants = flower.plants.all()
        if plants.count() > 0:
            return render(
                request,
                'plantjournal/flower_refuse_delete.html',
                {'flower': flower,
                 'plants': plants}
            )
        else:
            return render(
                request,
                'plantjournal/flower_confirm_delete.html',
                {'flower': flower}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Flower,
            pk=pk
        )

    def post(self, request, pk):
        flower = self.get_object(pk)
        flower.delete()
        return redirect('plantjournal_flower_list_urlpattern')


class PlantList(PageLinksMixin, ListView):
    paginate_by = 20
    model = Plant


class PlantDetail(View):

    def get(self, request, pk):
        plant = get_object_or_404(
            Plant,
            pk=pk
        )
        plant_latin_name = plant.plant_latin_name
        plant_description = plant.plant_description
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
             'plant_latin_name': plant_latin_name,
             'plant_description': plant_description,
             'light': light,
             'soil': soil,
             'humidity': humidity,
             'water': water,
             'fertilizer': fertilizer,
             'location': location,
             'toxicity': toxicity,
             'flower': flower,
             'growthinstance_list': growth_instance_list,
             'note_list': note_list}
        )


class PlantCreate(CreateView):
    form_class = PlantForm
    model = Plant


class PlantUpdate(UpdateView):
    form_class = PlantForm
    model = Plant
    template_name = 'plantjournal/plant_form_update.html'


class PlantDelete(View):

    def get(self, request, pk):
        plant = self.get_object(pk)
        notes = plant.notes.all()
        growth_instances = plant.growth_instances.all()
        if notes.count() > 0 or growth_instances.count() > 0:
            return render(
                request,
                'plantjournal/plant_refuse_delete.html',
                {'plant': plant,
                 'notes': notes,
                 'growthinstances': growth_instances}
            )
        else:
            return render(
                request,
                'plantjournal/plant_confirm_delete.html',
                {'plant': plant}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Plant,
            pk=pk
        )

    def post(self, request, pk):
        plant = self.get_object(pk)
        plant.delete()
        return redirect('plantjournal_plant_list_urlpattern')


class NoteList(PageLinksMixin, ListView):
    paginate_by = 20
    model = Note


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


class NoteCreate(CreateView):
    form_class = NoteForm
    model = Note


class NoteUpdate(UpdateView):
    form_class = NoteForm
    model = Note
    template_name = 'plantjournal/note_form_update.html'


class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('plantjournal_note_list_urlpattern')


class GrowthTypeList(ListView):
    model = GrowthType


class GrowthTypeDetail(View):

    def get(self, request, pk):
        growth_type = get_object_or_404(
            GrowthType,
            pk=pk
        )
        growth_instance_list = growth_type.growth_instances.all()
        return render(
            request,
            'plantjournal/growthtype_detail.html',
            {'growthtype': growth_type, 'growthinstance_list': growth_instance_list}
        )


class GrowthTypeCreate(CreateView):
    form_class = GrowthTypeForm
    model = GrowthType


class GrowthTypeUpdate(UpdateView):
    form_class = GrowthTypeForm
    model = GrowthType
    template_name = 'plantjournal/growthtype_form_update.html'


class GrowthTypeDelete(View):

    def get(self, request, pk):
        growth_type = self.get_object(pk)
        growth_instances = growth_type.growth_instances.all()
        if growth_instances.count() > 0:
            return render(
                request,
                'plantjournal/growthtype_refuse_delete.html',
                {'growthtype': growth_type,
                 'growthinstances': growth_instances}
            )
        else:
            return render(
                request,
                'plantjournal/growthtype_confirm_delete.html',
                {'growthtype': growth_type}
            )

    def get_object(self, pk):
        return get_object_or_404(
            GrowthType,
            pk=pk
        )

    def post(self, request, pk):
        growth_type = self.get_object(pk)
        growth_type.delete()
        return redirect('plantjournal_growthtype_list_urlpattern')


class GrowthInstanceList(PageLinksMixin, ListView):
    paginate_by = 20
    model = GrowthInstance


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
            'plantjournal/growthinstance_detail.html',
            {'growthinstance': growth_instance,
             'plant': plant,
             'growthtype': growth_type}
        )


class GrowthInstanceCreate(CreateView):
    form_class = GrowthInstanceForm
    model = GrowthInstance


class GrowthInstanceUpdate(UpdateView):
    form_class = GrowthInstanceForm
    model = GrowthInstance
    template_name = 'plantjournal/growthinstance_form_update.html'


class GrowthInstanceDelete(DeleteView):
    model = GrowthInstance
    success_url = reverse_lazy('plantjournal_growthinstance_list_urlpattern')
