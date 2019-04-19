from django.contrib import admin
from django.urls import path

from plantjournal.views import (
    light_list_view,
    soil_list_view,
    humidity_list_view,
    water_list_view,
    fertilizer_list_view,
    toxicity_list_view,
    location_list_view,
    flower_list_view,
    plant_list_view,
    note_list_view,
    growth_type_list_view,
    growth_instance_list_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('light/', light_list_view),
    path('soil/', soil_list_view),
    path('humidity/', humidity_list_view),
    path('water/', water_list_view),
    path('fertilizer/', fertilizer_list_view),
    path('toxicity/', toxicity_list_view),
    path('location/', location_list_view),
    path('flower/', flower_list_view),
    path('plant/', plant_list_view),
    path('note/', note_list_view),
    path('growth_type/', growth_type_list_view),
    path('growth_instance/', growth_instance_list_view),
]
