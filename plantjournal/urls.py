from django.urls import path

from plantjournal.views import (
    LightList,
    LightDetail,
    LightCreate,
    SoilList,
    SoilDetail,
    SoilCreate,
    HumidityList,
    HumidityDetail,
    HumidityCreate,
    WaterList,
    WaterDetail,
    WaterCreate,
    FertilizerList,
    FertilizerDetail,
    FertilizerCreate,
    LocationList,
    LocationDetail,
    LocationCreate,
    ToxicityList,
    ToxicityDetail,
    ToxicityCreate,
    FlowerList,
    FlowerDetail,
    FlowerCreate,
    PlantList,
    PlantDetail,
    PlantCreate,
    NoteList,
    NoteDetail,
    NoteCreate,
    GrowthTypeList,
    GrowthTypeDetail,
    GrowthTypeCreate,
    GrowthInstanceList,
    GrowthInstanceDetail,
    GrowthInstanceCreate,
)

urlpatterns = [

    path('light/',
         LightList.as_view(),
         name='plantjournal_light_list_urlpattern'),

    path('light/<int:pk>/',
         LightDetail.as_view(),
         name='plantjournal_light_detail_urlpattern'),

    path('light/create/',
         LightCreate.as_view(),
         name='plantjournal_light_create_urlpattern'),

    path('soil/',
         SoilList.as_view(),
         name='plantjournal_soil_list_urlpattern'),

    path('soil/<int:pk>/',
         SoilDetail.as_view(),
         name='plantjournal_soil_detail_urlpattern'),

    path('soil/create/',
         SoilCreate.as_view(),
         name='plantjournal_soil_create_urlpattern'),

    path('humidity/',
         HumidityList.as_view(),
         name='plantjournal_humidity_list_urlpattern'),

    path('humidity/<int:pk>/',
         HumidityDetail.as_view(),
         name='plantjournal_humidity_detail_urlpattern'),

    path('humidity/create/',
         HumidityCreate.as_view(),
         name='plantjournal_humidity_create_urlpattern'),

    path('water/',
         WaterList.as_view(),
         name='plantjournal_water_list_urlpattern'),

    path('water/<int:pk>/',
         WaterDetail.as_view(),
         name='plantjournal_water_detail_urlpattern'),

    path('water/create/',
         WaterCreate.as_view(),
         name='plantjournal_water_create_urlpattern'),

    path('fertilizer/',
         FertilizerList.as_view(),
         name='plantjournal_fertilizer_list_urlpattern'),

    path('fertilizer/<int:pk>/',
         FertilizerDetail.as_view(),
         name='plantjournal_fertilizer_detail_urlpattern'),

    path('fertilizer/create/',
         FertilizerCreate.as_view(),
         name='plantjournal_fertilizer_create_urlpattern'),

    path('location/',
         LocationList.as_view(),
         name='plantjournal_location_list_urlpattern'),

    path('location/<int:pk>/',
         LocationDetail.as_view(),
         name='plantjournal_location_detail_urlpattern'),

    path('location/create/',
         LocationCreate.as_view(),
         name='plantjournal_location_create_urlpattern'),

    path('toxicity/',
         ToxicityList.as_view(),
         name='plantjournal_toxicity_list_urlpattern'),

    path('toxicity/<int:pk>/',
         ToxicityDetail.as_view(),
         name='plantjournal_toxicity_detail_urlpattern'),

    path('toxicity/create/',
         ToxicityCreate.as_view(),
         name='plantjournal_toxicity_create_urlpattern'),

    path('flower/',
         FlowerList.as_view(),
         name='plantjournal_flower_list_urlpattern'),

    path('flower/<int:pk>/',
         FlowerDetail.as_view(),
         name='plantjournal_flower_detail_urlpattern'),

    path('flower/create/',
         FlowerCreate.as_view(),
         name='plantjournal_flower_create_urlpattern'),

    path('plant/',
         PlantList.as_view(),
         name='plantjournal_plant_list_urlpattern'),

    path('plant/<int:pk>/',
         PlantDetail.as_view(),
         name='plantjournal_plant_detail_urlpattern'),

    path('plant/create/',
         PlantCreate.as_view(),
         name='plantjournal_plant_create_urlpattern'),

    path('note/',
         NoteList.as_view(),
         name='plantjournal_note_list_urlpattern'),

    path('note/<int:pk>/',
         NoteDetail.as_view(),
         name='plantjournal_note_detail_urlpattern'),

    path('note/create/',
         NoteCreate.as_view(),
         name='plantjournal_note_create_urlpattern'),

    path('growth_type/',
         GrowthTypeList.as_view(),
         name='plantjournal_growth_type_list_urlpattern'),

    path('growth_type/<int:pk>/',
         GrowthTypeDetail.as_view(),
         name='plantjournal_growth_type_detail_urlpattern'),

    path('growth_type/create/',
         GrowthTypeCreate.as_view(),
         name='plantjournal_growth_type_create_urlpattern'),

    path('growth_instance/',
         GrowthInstanceList.as_view(),
         name='plantjournal_growth_instance_list_urlpattern'),

    path('growth_instance/<int:pk>/',
         GrowthInstanceDetail.as_view(),
         name='plantjournal_growth_instance_detail_urlpattern'),

    path('growth_instance/create/',
         GrowthInstanceCreate.as_view(),
         name='plantjournal_growth_instance_create_urlpattern'),

]
