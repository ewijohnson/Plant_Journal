from django.shortcuts import render, get_object_or_404, redirect
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


class GrowthTypeUpdate(View):
    form_class = GrowthTypeForm
    model = GrowthType
    template_name = 'plantjournal/growth_type_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        growth_type = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=growth_type),
            'growth_type': growth_type
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
                'growth_type': growth_type
            }
            return render(
                request,
                self.template_name,
                context)


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


class GrowthInstanceUpdate(View):
    form_class = GrowthInstanceForm
    model = GrowthInstance
    template_name = 'plantjournal/growth_instance_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        growth_instance = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=growth_instance),
            'growth_instance': growth_instance
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
                'growth_instance': growth_instance
            }
            return render(
                request,
                self.template_name,
                context)
