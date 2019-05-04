from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView

from plantjournal.forms import LightForm, SoilForm, HumidityForm, WaterForm, FertilizerForm, LocationForm, \
    ToxicityForm, FlowerForm, PlantForm, NoteForm, GrowthTypeForm, GrowthInstanceForm
from plantjournal.utils import ObjectCreateMixin, PageLinksMixin

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


class LightList(PageLinksMixin, ListView):
    paginate_by = 20
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


class LightCreate(ObjectCreateMixin, View):
    form_class = LightForm
    template_name = 'plantjournal/light_form.html'


class LightUpdate(View):
    form_class = LightForm
    model = Light
    template_name = 'plantjournal/light_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        light = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=light),
            'light': light
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        light = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=light)
        if bound_form.is_valid():
            new_light = bound_form.save()
            return redirect(new_light)
        else:
            context = {
                'form': bound_form,
                'light': light
            }
            return render(
                request,
                self.template_name,
                context)


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


class SoilCreate(ObjectCreateMixin, View):
    form_class = SoilForm
    template_name = 'plantjournal/soil_form.html'


class SoilUpdate(View):
    form_class = SoilForm
    model = Soil
    template_name = 'plantjournal/soil_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        soil = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=soil),
            'soil': soil
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        soil = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=soil)
        if bound_form.is_valid():
            new_soil = bound_form.save()
            return redirect(new_soil)
        else:
            context = {
                'form': bound_form,
                'soil': soil
            }
            return render(
                request,
                self.template_name,
                context)


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


class HumidityList(PageLinksMixin, ListView):
    paginate_by = 20
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


class HumidityCreate(ObjectCreateMixin, View):
    form_class = HumidityForm
    template_name = 'plantjournal/humidity_form.html'


class HumidityUpdate(View):
    form_class = HumidityForm
    model = Humidity
    template_name = 'plantjournal/humidity_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        humidity = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=humidity),
            'humidity': humidity
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        humidity = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=humidity)
        if bound_form.is_valid():
            new_humidity = bound_form.save()
            return redirect(new_humidity)
        else:
            context = {
                'form': bound_form,
                'humidity': humidity
            }
            return render(
                request,
                self.template_name,
                context)


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


class WaterCreate(ObjectCreateMixin, View):
    form_class = WaterForm
    template_name = 'plantjournal/water_form.html'


class WaterUpdate(View):
    form_class = WaterForm
    model = Water
    template_name = 'plantjournal/water_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        water = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=water),
            'water': water
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        water = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=water)
        if bound_form.is_valid():
            new_water = bound_form.save()
            return redirect(new_water)
        else:
            context = {
                'form': bound_form,
                'water': water
            }
            return render(
                request,
                self.template_name,
                context)


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


class FertilizerCreate(ObjectCreateMixin, View):
    form_class = FertilizerForm
    template_name = 'plantjournal/fertilizer_form.html'


class FertilizerUpdate(View):
    form_class = FertilizerForm
    model = Fertilizer
    template_name = 'plantjournal/fertilizer_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        fertilizer = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=fertilizer),
            'fertilizer': fertilizer
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        fertilizer = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=fertilizer)
        if bound_form.is_valid():
            new_fertilizer = bound_form.save()
            return redirect(new_fertilizer)
        else:
            context = {
                'form': bound_form,
                'fertilizer': fertilizer
            }
            return render(
                request,
                self.template_name,
                context)


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


class LocationCreate(ObjectCreateMixin, View):
    form_class = LocationForm
    template_name = 'plantjournal/location_form.html'


class LocationUpdate(View):
    form_class = LocationForm
    model = Location
    template_name = 'plantjournal/location_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        location = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=location),
            'location': location
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        location = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=location)
        if bound_form.is_valid():
            new_location = bound_form.save()
            return redirect(new_location)
        else:
            context = {
                'form': bound_form,
                'location': location
            }
            return render(
                request,
                self.template_name,
                context)


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


class ToxicityList(PageLinksMixin, ListView):
    paginate_by = 20
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


class ToxicityCreate(ObjectCreateMixin, View):
    form_class = ToxicityForm
    template_name = 'plantjournal/toxicity_form.html'


class ToxicityUpdate(View):
    form_class = ToxicityForm
    model = Toxicity
    template_name = 'plantjournal/toxicity_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        toxicity = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=toxicity),
            'toxicity': toxicity
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        toxicity = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=toxicity)
        if bound_form.is_valid():
            new_toxicity = bound_form.save()
            return redirect(new_toxicity)
        else:
            context = {
                'form': bound_form,
                'toxicity': toxicity
            }
            return render(
                request,
                self.template_name,
                context)


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


class FlowerCreate(ObjectCreateMixin, View):
    form_class = FlowerForm
    template_name = 'plantjournal/flower_form.html'


class FlowerUpdate(View):
    form_class = FlowerForm
    model = Flower
    template_name = 'plantjournal/flower_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        flower = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=flower),
            'flower': flower
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        flower = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=flower)
        if bound_form.is_valid():
            new_flower = bound_form.save()
            return redirect(new_flower)
        else:
            context = {
                'form': bound_form,
                'flower': flower
            }
            return render(
                request,
                self.template_name,
                context)


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


class PlantCreate(ObjectCreateMixin, View):
    form_class = PlantForm
    template_name = 'plantjournal/plant_form.html'


class PlantUpdate(View):
    form_class = PlantForm
    model = Plant
    template_name = 'plantjournal/plant_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        plant = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=plant),
            'plant': plant
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        plant = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=plant)
        if bound_form.is_valid():
            new_plant = bound_form.save()
            return redirect(new_plant)
        else:
            context = {
                'form': bound_form,
                'plant': plant
            }
            return render(
                request,
                self.template_name,
                context)


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


class NoteCreate(ObjectCreateMixin, View):
    form_class = NoteForm
    template_name = 'plantjournal/note_form.html'


class NoteUpdate(View):
    form_class = NoteForm
    model = Note
    template_name = 'plantjournal/note_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        note = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=note),
            'note': note
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        note = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=note)
        if bound_form.is_valid():
            new_note = bound_form.save()
            return redirect(new_note)
        else:
            context = {
                'form': bound_form,
                'note': note
            }
            return render(
                request,
                self.template_name,
                context)


class NoteDelete(View):

    def get(self, request, pk):
        note = self.get_object(pk)
        return render(
            request,
            'plantjournal/note_confirm_delete.html',
            {'note': note}
        )

    def get_object(self, pk):
        return get_object_or_404(
            Note,
            pk=pk
        )

    def post(self, request, pk):
        note = self.get_object(pk)
        note.delete()
        return redirect('plantjournal_note_list_urlpattern')


class GrowthTypeList(PageLinksMixin, ListView):
    paginate_by = 20
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


class GrowthTypeCreate(ObjectCreateMixin, View):
    form_class = GrowthTypeForm
    template_name = 'plantjournal/growthtype_form.html'


class GrowthTypeUpdate(View):
    form_class = GrowthTypeForm
    model = GrowthType
    template_name = 'plantjournal/growthtype_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        growth_type = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=growth_type),
            'growthtype': growth_type
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        growth_type = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=growth_type)
        if bound_form.is_valid():
            new_growth_type = bound_form.save()
            return redirect(new_growth_type)
        else:
            context = {
                'form': bound_form,
                'growthtype': growth_type
            }
            return render(
                request,
                self.template_name,
                context)


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


class GrowthInstanceCreate(ObjectCreateMixin, View):
    form_class = GrowthInstanceForm
    template_name = 'plantjournal/growthinstance_form.html'


class GrowthInstanceUpdate(View):
    form_class = GrowthInstanceForm
    model = GrowthInstance
    template_name = 'plantjournal/growthinstance_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        growth_instance = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=growth_instance),
            'growthinstance': growth_instance
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        growth_instance = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=growth_instance)
        if bound_form.is_valid():
            new_growth_instance = bound_form.save()
            return redirect(new_growth_instance)
        else:
            context = {
                'form': bound_form,
                'growthinstance': growth_instance
            }
            return render(
                request,
                self.template_name,
                context)


class GrowthInstanceDelete(View):

    def get(self, request, pk):
        growth_instance = self.get_object(pk)
        return render(
            request,
            'plantjournal/growthinstance_confirm_delete.html',
            {'growthinstance': growth_instance}
        )

    def get_object(self, pk):
        return get_object_or_404(
            GrowthInstance,
            pk=pk
        )

    def post(self, request, pk):
        growth_instance = self.get_object(pk)
        growth_instance.delete()
        return redirect('plantjournal_growthinstance_list_urlpattern')
