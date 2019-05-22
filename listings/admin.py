from django.contrib import admin
from .models import Listing
class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_publish', 'price', 'list_date', 'realtor')
  list_display_links = ('id', 'title')
  list_filter = ('realtor',)
  list_editable = ('is_publish',)
  search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'is_publish', 'list_date', 'price', 'bedrooms', 'bathrooms')
  list_per_page = 25

admin.site.register(Listing, ListingAdmin)
