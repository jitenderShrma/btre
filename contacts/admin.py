from django.contrib import admin

class ContactsAdmin(admin.ModelAdmin):

  list_display = ('id', 'name', 'listing', 'email', 'contact', 'contact_date')
  list_display_links = ('id', 'name', 'listing')
  search_fields = ('name', 'listing', 'email')
  list_per_page = 25

from .models import Contact

admin.site.register(Contact, ContactsAdmin)