from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import bedroom_choices, prices_choices, state_choices



def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_publish=True)
  print(len(listings))
  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  page_listings = paginator.get_page(page)
  content = {
    'listings': page_listings
  }
  return render(request, 'listings/listings.html', content)

def listing(request, listing_id):

  listing = get_object_or_404(Listing, pk=listing_id)
  content = {
    'listing': listing
  }
  return render(request, 'listings/listing.html', content)

def search(request):
  print(request.GET)
  queryset_list = Listing.objects.order_by('-list_date')
  
  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    queryset_list = queryset_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)

  # Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  choices = {
    'bedroom_choices': bedroom_choices,
    'price_choices': prices_choices,
    'state_choices': state_choices,
    'listings': queryset_list,
    'values': request.GET
  }
  return render(request, 'listings/search.html', choices)