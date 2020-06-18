from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.core.mail import send_mail
from django.conf import settings
from accounts.models import Company, Shipment
from .forms import ShipmentForm
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from home.serializers import UserSerializer, GroupSerializer, CompanySerializer, ShipmentSerializer
from django.forms.models import model_to_dict

class Login(generic.DetailView):
    template_name = 'home/login.html'




def profile(request):
    shipments = Shipment.objects.all()
    content = {"shipments": shipment}
    return render(request, 'home/profile.html', content)

def get_shipment(request):
    # if this is a POST request we need to process the form data
    shipment = Shipment()
    user = request.user
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ShipmentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            shipment.user_name = user
            shipment.company_name = user.company
            shipment.shipment_date = form.cleaned_data['date']
            shipment.total_price = form.cleaned_data['total_price']
            shipment.tracking_number = form.cleaned_data['tracking_number']
            shipment.service_level = form.cleaned_data['service_level']
            shipment.destination = form.cleaned_data['destination']
            shipment.ref_1 = form.cleaned_data['ref_1']
            shipment.ref_2 = form.cleaned_data['ref_2']
            shipment.weight = form.cleaned_data['weight']
            shipment.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/accounts/profile')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ShipmentForm()

    return render(request, 'home/add_shipment.html', {'form': form})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class ShipmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer