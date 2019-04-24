from django import forms

from plantjournal.models import Light, Soil, Humidity, Water, Fertilizer, Location, Toxicity, Flower, Plant, Note, \
    GrowthType, GrowthInstance


class LightForm(forms.ModelForm):

    class Meta:
        model = Light
        fields = '__all__'

    def clean_light_type(self):
        return self.cleaned_data['light_type'].strip()


class SoilForm(forms.ModelForm):

    class Meta:
        model = Soil
        fields = '__all__'

    def clean_soil_type(self):
        return self.cleaned_data['soil_type'].strip()


class HumidityForm(forms.ModelForm):

    class Meta:
        model = Humidity
        fields = '__all__'

    def clean_humidity_level(self):
        return self.cleaned_data['humidity_level'].strip()


class WaterForm(forms.ModelForm):

    class Meta:
        model = Water
        fields = '__all__'

    def clean_water_freq(self):
        return self.cleaned_data['water_freq'].strip()

    def clean_water_type(self):
        return self.cleaned_data['water_type'].strip()


class FertilizerForm(forms.ModelForm):

    class Meta:
        model = Fertilizer
        fields = '__all__'

    def clean_fertilizer_freq(self):
        return self.cleaned_data['fertilizer_freq'].strip()

    def clean_fertilizer_type(self):
        return self.cleaned_data['fertilizer_type'].strip()


class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = '__all__'

    def clean_location_name(self):
        return self.cleaned_data['location_name'].strip()


class ToxicityForm(forms.ModelForm):

    class Meta:
        model = Toxicity
        fields = '__all__'

    def clean_toxicity_type(self):
        return self.cleaned_data['toxicity_type'].strip()


class FlowerForm(forms.ModelForm):

    class Meta:
        model = Flower
        fields = '__all__'

    def clean_flower_type(self):
        return self.cleaned_data['flower_type'].strip()


class PlantForm(forms.ModelForm):

    class Meta:
        model = Plant
        fields = '__all__'

    def clean_plant_name(self):
        return self.cleaned_data['plant_name'].strip()

    def clean_plant_number(self):
        return self.cleaned_data['plant_number'].strip()

    def clean_plant_nickname(self):
        return self.cleaned_data['plant_nickname'].strip()

    def clean_plant_latin_name(self):
        return self.cleaned_data['plant_latin_name'].strip()

    def clean_plant_description(self):
        return self.cleaned_data['plant_description'].strip()


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = '__all__'

    def clean_note_name(self):
        return self.cleaned_data['note_name'].strip()

    def clean_note_body(self):
        return self.cleaned_data['note_body'].strip()


class GrowthTypeForm(forms.ModelForm):

    class Meta:
        model = GrowthType
        fields = '__all__'

    def clean_growth_type_name(self):
        return self.cleaned_data['growth_type_name'].strip()


class GrowthInstanceForm(forms.ModelForm):

    class Meta:
        model = GrowthInstance
        fields = '__all__'
