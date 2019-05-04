from __future__ import unicode_literals
from itertools import chain

from django.db import migrations


def populate_permissions_lists(apps):
    permission_class = apps.get_model('auth', 'Permission')

    light_permissions = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                        content_type__model='light')

    soil_permissions = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                       content_type__model='soil')

    humidity_permissions = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                           content_type__model='humidity')

    water_permissions = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                        content_type__model='water')

    fertilizer_permissions = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                             content_type__model='fertilizer')

    location_permissions = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                           content_type__model='location')

    toxicity_permissions = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                           content_type__model='toxicity')

    flower_permissions = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                         content_type__model='flower')

    plant_permissions = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                        content_type__model='plant')

    note_permissions = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                       content_type__model='note')

    growthtype_permissions = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                             content_type__model='growthtype')

    growthinstance_permissions = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                                 content_type__model='growthinstance')

    perm_view_light = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                      content_type__model='light',
                                                      codename='view_light')

    perm_view_soil = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                     content_type__model='soil',
                                                     codename='view_soil')

    perm_view_humidity = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                         content_type__model='humidity',
                                                         codename='view_humidity')

    perm_view_water = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                      content_type__model='water',
                                                      codename='view_water')

    perm_view_fertilizer = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                           content_type__model='fertilizer',
                                                           codename='view_fertilizer')

    perm_view_location = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                         content_type__model='location',
                                                         codename='view_location')

    perm_view_toxicity = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                         content_type__model='toxicity',
                                                         codename='view_toxicity')

    perm_view_flower = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                       content_type__model='flower',
                                                       codename='view_flower')

    perm_view_plant = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                      content_type__model='plant',
                                                      codename='view_plant')

    perm_view_note = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                     content_type__model='note',
                                                     codename='view_note')

    perm_view_growthtype = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                           content_type__model='growthtype',
                                                           codename='view_growthtype')

    perm_view_growthinstance = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                               content_type__model='growthinstance',
                                                               codename='view_growthinstance')

    perm_add_plant = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                     content_type__model='plant',
                                                     codename='add_plant')

    perm_add_note = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                    content_type__model='note',
                                                    codename='add_note')

    perm_add_growthinstance = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                              content_type__model='growthinstance',
                                                              codename='add_growthinstance')

    perm_change_plant = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                        content_type__model='plant',
                                                        codename='change_plant')

    perm_change_note = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                       content_type__model='note',
                                                       codename='change_note')

    perm_change_growthinstance = permission_class.objects.filter(content_type__app_label='plantjournal',
                                                                 content_type__model='growthinstance',
                                                                 codename='change_growthinstance')

    pj_guest_permissions = chain(perm_view_light,
                                 perm_view_soil,
                                 perm_view_humidity,
                                 perm_view_water,
                                 perm_view_fertilizer,
                                 perm_view_location,
                                 perm_view_toxicity,
                                 perm_view_flower,
                                 perm_view_plant,
                                 perm_view_note,
                                 perm_view_growthtype,
                                 perm_view_growthinstance)

    pj_user_permissions = chain(perm_view_light,
                                perm_view_soil,
                                perm_view_humidity,
                                perm_view_water,
                                perm_view_fertilizer,
                                perm_view_location,
                                perm_view_toxicity,
                                perm_view_flower,
                                perm_view_plant,
                                perm_view_note,
                                perm_view_growthtype,
                                perm_view_growthinstance,
                                perm_add_plant,
                                perm_add_note,
                                perm_add_growthinstance,
                                perm_change_plant,
                                perm_change_note,
                                perm_change_growthinstance)

    pj_admin_permissions = chain(light_permissions,
                                 soil_permissions,
                                 humidity_permissions,
                                 water_permissions,
                                 fertilizer_permissions,
                                 location_permissions,
                                 toxicity_permissions,
                                 flower_permissions,
                                 plant_permissions,
                                 note_permissions,
                                 growthtype_permissions,
                                 growthinstance_permissions)

    my_groups_initialization_list = [
        {
            "name": "pj_guest",
            "permissions_list": pj_guest_permissions,
        },
        {
            "name": "pj_user",
            "permissions_list": pj_user_permissions,
        },
        {
            "name": "pj_admin",
            "permissions_list": pj_admin_permissions,
        },
    ]
    return my_groups_initialization_list


def add_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    Group = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = Group.objects.get(
                name=group['name']
            )
            group_object.permissions.set(group['permissions_list'])
            group_object.save()


def remove_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    Group = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = Group.objects.get(
                name=group['name']
            )
            list_of_permissions = group['permissions_list']
            for permission in list_of_permissions:
                group_object.permissions.remove(permission)
                group_object.save()


class Migration(migrations.Migration):
    dependencies = [
        ('plantjournal', '0012_create_groups'),
    ]

    operations = [
        migrations.RunPython(
            add_group_permissions_data,
            remove_group_permissions_data
        )
    ]
