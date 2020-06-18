from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Shipment
from django.core.paginator import Paginator

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = 'accounts/login.html'
    template_name = 'accounts/signup.html'

class Login(generic.CreateView):
    template_name = 'accounts/login.html'






def index(request):
    shipments = Shipment.objects.all()
    paginator = Paginator(shipments, 2) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'home/profile.html', {'page_obj': page_obj})

