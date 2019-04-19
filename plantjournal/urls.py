from django.urls import path

from plantjournal.views import (
    LightList,
    SoilList,
    HumidityList,
    WaterList,
    FertilizerList,
    ToxicityList,
    LocationList,
    FlowerList,
    PlantList,
    NoteList,
    GrowthTypeList,
    GrowthInstanceList,
)

urlpatterns = [

    path('light/',
         LightList.as_view(),
         name='plantjournal_light_list_urlpattern'),

    path('soil/',
         SoilList.as_view(),
         name='plantjournal_soil_list_urlpattern'),

    path('humidity/',
         HumidityList.as_view(),
         name='plantjournal_humidity_list_urlpattern'),

    path('water/',
         WaterList.as_view(),
         name='plantjournal_water_list_urlpattern'),

    path('fertilizer/',
         FertilizerList.as_view(),
         name='plantjournal_fertilizer_list_urlpattern'),

    path('toxicity/',
         ToxicityList.as_view(),
         name='plantjournal_toxicity_list_urlpattern'),

    path('location/',
         LocationList.as_view(),
         name='plantjournal_location_list_urlpattern'),

    path('flower/',
         FlowerList.as_view(),
         name='plantjournal_flower_list_urlpattern'),

    path('plant/',
         PlantList.as_view(),
         name='plantjournal_plant_list_urlpattern'),

    path('note/',
         NoteList.as_view(),
         name='plantjournal_note_list_urlpattern'),

    path('growth_type/',
         GrowthTypeList.as_view(),
         name='plantjournal_growth_type_list_urlpattern'),

    path('growth_instance/',
         GrowthInstanceList.as_view(),
         name='plantjournal_growth_instance_list_urlpattern'),

]
