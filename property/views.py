from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from property.forms import PropertyForm, PropertyCommentForm
from property.models import Property, PropertyComment


@login_required
def home(request):
    properties = Property.objects.filter(contributors=request.user)
    return render(request, "property/home.html",
                  {'properties': properties})


@login_required
def view_property(request, property_id):
    property = get_object_or_404(
        Property.objects.filter(contributors=request.user),
        id=property_id)
    comments = PropertyComment.objects.filter(
        user__in=property.contributors.all(),
        property=property)
    comment_form = PropertyCommentForm()
    return render(request, "property/view_property.html",
                  {"property": property,
                   "comments": comments,
                   "comment_form": comment_form})


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


@login_required
def add_comment(request, property_id):
    property = get_object_or_404(
        Property.objects.filter(contributors=request.user),
        id=property_id)
    if request.POST:
        form = PropertyCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.property = property
            comment.save()
    return redirect("view-property", property.id)
