from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import bedroom_choices, prices_choices, state_choices

# models
from listings.models import Listing
from realtors.models import Realtor

def index(request):
  
  # Get Listing
  listings = Listing.objects.order_by('-list_date').filter(is_publish=True)[:3]
  content = {
    'listings': listings,
    'bedroom_choices': bedroom_choices,
    'price_choices': prices_choices,
    'state_choices': state_choices
  }

  return render(request, 'pages/index.html', content)

def about(request):
  
  # Get realtors
  realtors = Realtor.objects.order_by('-hire_date')

  # Get mvp_realtors
  mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
  content = {
    'realtors': realtors,
    'mvp_realtors': mvp_realtors
  }
  return render(request, 'pages/about.html', content)
