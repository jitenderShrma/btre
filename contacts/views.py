from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

def contact(request):
  
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    realtor_email = request.POST['realtor_email']
    message = request.POST['message']
    email = request.POST['email']
    user_id = request.POST['user_id']
    name = request.POST['name']
    contact = request.POST['phone']
    
    # Check if user has inquiry already
    if request.user.is_authenticated:
      contacted_has = Contact.objects.all().filter(listing_id=listing_id, user_id=request.user.id)
      if contacted_has:
        messages.error(request, 'You have already make inquiry for this listing')
        return redirect('/listing/'+listing_id)

    contact = Contact(listing_id=listing_id, listing=listing, realtor_email=realtor_email, message=message, email=email, user_id=user_id, name=name, contact=contact)
    contact.save()

    # Send gmail
    send_mail(
      'Property Listing Inquiry',
      'There has Inquiry for ' + listing + 'for more info login admin',
      'jitenderkanti020@gmail.com',
      [realtor_email, 'jitenderkumar946799@gmail.com'],
      fail_silently=False
    )

    messages.success(request, 'Your inquiry is submitted, a realtor will get back to you')
    return redirect('/listing/'+listing_id)
