from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from property.forms import PropertyForm
from property.models import Property


@login_required
def home(request):
    properties = Property.objects.filter(user=request.user)
    return render(request, "property/home.html", {'properties': properties})


@login_required
def add_update_property(request, property_id=None):
    property = None
    if property_id:
        property = get_object_or_404(
            Property, id=property_id, user=request.user)

    form = PropertyForm(instance=property)
    if request.POST:
        form = PropertyForm(data=request.POST, instance=property)
        if form.is_valid():
            property = form.save(commit=False)
            property.user = request.user
            property.save()
            return redirect("update-property", property.id)
    return render(
        request,
        "property/add_update_property.html",
        {'form': form})
