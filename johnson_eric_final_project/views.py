from django.shortcuts import redirect


def redirect_root_view(request):
    return redirect('plantjournal_plant_list_urlpattern')
