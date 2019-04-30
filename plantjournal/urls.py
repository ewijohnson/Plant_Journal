from django.urls import path

from plantjournal.views import (
    LightList,
    LightDetail,
    LightCreate,
    LightUpdate,
    LightDelete,
    SoilList,
    SoilDetail,
    SoilCreate,
    SoilUpdate,
    SoilDelete,
    HumidityList,
    HumidityDetail,
    HumidityCreate,
    HumidityUpdate,
    HumidityDelete,
    WaterList,
    WaterDetail,
    WaterCreate,
    WaterUpdate,
    WaterDelete,
    FertilizerList,
    FertilizerDetail,
    FertilizerCreate,
    FertilizerUpdate,
    FertilizerDelete,
    LocationList,
    LocationDetail,
    LocationCreate,
    LocationUpdate,
    LocationDelete,
    ToxicityList,
    ToxicityDetail,
    ToxicityCreate,
    ToxicityUpdate,
    ToxicityDelete,
    FlowerList,
    FlowerDetail,
    FlowerCreate,
    FlowerUpdate,
    FlowerDelete,
    PlantList,
    PlantDetail,
    PlantCreate,
    PlantUpdate,
    PlantDelete,
    NoteList,
    NoteDetail,
    NoteCreate,
    NoteUpdate,
    NoteDelete,
    GrowthTypeList,
    GrowthTypeDetail,
    GrowthTypeCreate,
    GrowthTypeUpdate,
    GrowthTypeDelete,
    GrowthInstanceList,
    GrowthInstanceDetail,
    GrowthInstanceCreate,
    GrowthInstanceUpdate,
    GrowthInstanceDelete,
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

    path('light/<int:pk>/update/',
         LightUpdate.as_view(),
         name='plantjournal_light_update_urlpattern'),

    path('light/<int:pk>/delete/',
         LightDelete.as_view(),
         name='plantjournal_light_delete_urlpattern'),

    path('soil/',
         SoilList.as_view(),
         name='plantjournal_soil_list_urlpattern'),

    path('soil/<int:pk>/',
         SoilDetail.as_view(),
         name='plantjournal_soil_detail_urlpattern'),

    path('soil/create/',
         SoilCreate.as_view(),
         name='plantjournal_soil_create_urlpattern'),

    path('soil/<int:pk>/update/',
         SoilUpdate.as_view(),
         name='plantjournal_soil_update_urlpattern'),

    path('soil/<int:pk>/delete/',
         SoilDelete.as_view(),
         name='plantjournal_soil_delete_urlpattern'),

    path('humidity/',
         HumidityList.as_view(),
         name='plantjournal_humidity_list_urlpattern'),

    path('humidity/<int:pk>/',
         HumidityDetail.as_view(),
         name='plantjournal_humidity_detail_urlpattern'),

    path('humidity/create/',
         HumidityCreate.as_view(),
         name='plantjournal_humidity_create_urlpattern'),

    path('humidity/<int:pk>/update/',
         HumidityUpdate.as_view(),
         name='plantjournal_humidity_update_urlpattern'),

    path('humidity/<int:pk>/delete/',
         HumidityDelete.as_view(),
         name='plantjournal_humidity_delete_urlpattern'),

    path('water/',
         WaterList.as_view(),
         name='plantjournal_water_list_urlpattern'),

    path('water/<int:pk>/',
         WaterDetail.as_view(),
         name='plantjournal_water_detail_urlpattern'),

    path('water/create/',
         WaterCreate.as_view(),
         name='plantjournal_water_create_urlpattern'),

    path('water/<int:pk>/update/',
         WaterUpdate.as_view(),
         name='plantjournal_water_update_urlpattern'),

    path('water/<int:pk>/delete/',
         WaterDelete.as_view(),
         name='plantjournal_water_delete_urlpattern'),

    path('fertilizer/',
         FertilizerList.as_view(),
         name='plantjournal_fertilizer_list_urlpattern'),

    path('fertilizer/<int:pk>/',
         FertilizerDetail.as_view(),
         name='plantjournal_fertilizer_detail_urlpattern'),

    path('fertilizer/create/',
         FertilizerCreate.as_view(),
         name='plantjournal_fertilizer_create_urlpattern'),

    path('fertilizer/<int:pk>/update/',
         FertilizerUpdate.as_view(),
         name='plantjournal_fertilizer_update_urlpattern'),

    path('fertilizer/<int:pk>/delete/',
         FertilizerDelete.as_view(),
         name='plantjournal_fertilizer_delete_urlpattern'),

    path('location/',
         LocationList.as_view(),
         name='plantjournal_location_list_urlpattern'),

    path('location/<int:pk>/',
         LocationDetail.as_view(),
         name='plantjournal_location_detail_urlpattern'),

    path('location/create/',
         LocationCreate.as_view(),
         name='plantjournal_location_create_urlpattern'),

    path('location/<int:pk>/update/',
         LocationUpdate.as_view(),
         name='plantjournal_location_update_urlpattern'),

    path('location/<int:pk>/delete/',
         LocationDelete.as_view(),
         name='plantjournal_location_delete_urlpattern'),

    path('toxicity/',
         ToxicityList.as_view(),
         name='plantjournal_toxicity_list_urlpattern'),

    path('toxicity/<int:pk>/',
         ToxicityDetail.as_view(),
         name='plantjournal_toxicity_detail_urlpattern'),

    path('toxicity/create/',
         ToxicityCreate.as_view(),
         name='plantjournal_toxicity_create_urlpattern'),

    path('toxicity/<int:pk>/update/',
         ToxicityUpdate.as_view(),
         name='plantjournal_toxicity_update_urlpattern'),

    path('toxicity/<int:pk>/delete/',
         ToxicityDelete.as_view(),
         name='plantjournal_toxicity_delete_urlpattern'),

    path('flower/',
         FlowerList.as_view(),
         name='plantjournal_flower_list_urlpattern'),

    path('flower/<int:pk>/',
         FlowerDetail.as_view(),
         name='plantjournal_flower_detail_urlpattern'),

    path('flower/create/',
         FlowerCreate.as_view(),
         name='plantjournal_flower_create_urlpattern'),

    path('flower/<int:pk>/update/',
         FlowerUpdate.as_view(),
         name='plantjournal_flower_update_urlpattern'),

    path('flower/<int:pk>/delete/',
         FlowerDelete.as_view(),
         name='plantjournal_flower_delete_urlpattern'),

    path('plant/',
         PlantList.as_view(),
         name='plantjournal_plant_list_urlpattern'),

    path('plant/<int:pk>/',
         PlantDetail.as_view(),
         name='plantjournal_plant_detail_urlpattern'),

    path('plant/create/',
         PlantCreate.as_view(),
         name='plantjournal_plant_create_urlpattern'),

    path('plant/<int:pk>/update/',
         PlantUpdate.as_view(),
         name='plantjournal_plant_update_urlpattern'),

    path('plant/<int:pk>/delete/',
         PlantDelete.as_view(),
         name='plantjournal_plant_delete_urlpattern'),

    path('note/',
         NoteList.as_view(),
         name='plantjournal_note_list_urlpattern'),

    path('note/<int:pk>/',
         NoteDetail.as_view(),
         name='plantjournal_note_detail_urlpattern'),

    path('note/create/',
         NoteCreate.as_view(),
         name='plantjournal_note_create_urlpattern'),

    path('note/<int:pk>/update/',
         NoteUpdate.as_view(),
         name='plantjournal_note_update_urlpattern'),

    path('note/<int:pk>/delete/',
         NoteDelete.as_view(),
         name='plantjournal_note_delete_urlpattern'),

    path('growth_type/',
         GrowthTypeList.as_view(),
         name='plantjournal_growth_type_list_urlpattern'),

    path('growth_type/<int:pk>/',
         GrowthTypeDetail.as_view(),
         name='plantjournal_growth_type_detail_urlpattern'),

    path('growth_type/create/',
         GrowthTypeCreate.as_view(),
         name='plantjournal_growth_type_create_urlpattern'),

    path('growth_type/<int:pk>/update/',
         GrowthTypeUpdate.as_view(),
         name='plantjournal_growth_type_update_urlpattern'),

    path('growth_type/<int:pk>/delete/',
         GrowthTypeDelete.as_view(),
         name='plantjournal_growth_type_delete_urlpattern'),

    path('growth_instance/',
         GrowthInstanceList.as_view(),
         name='plantjournal_growth_instance_list_urlpattern'),

    path('growth_instance/<int:pk>/',
         GrowthInstanceDetail.as_view(),
         name='plantjournal_growth_instance_detail_urlpattern'),

    path('growth_instance/create/',
         GrowthInstanceCreate.as_view(),
         name='plantjournal_growth_instance_create_urlpattern'),

    path('growth_instance/<int:pk>/update/',
         GrowthInstanceUpdate.as_view(),
         name='plantjournal_growth_instance_update_urlpattern'),

    path('growth_instance/<int:pk>/delete/',
         GrowthInstanceDelete.as_view(),
         name='plantjournal_growth_instance_delete_urlpattern'),

]
