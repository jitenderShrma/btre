from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def login(request):

  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    # User exist
    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid credentials')
      content = {
        'username': username
      }
      return render(request, 'accounts/login.html', content)
  else:
    return render(request, 'accounts/login.html')

def register(request):

  if request.method == 'POST':
    
    # Get fields
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Validate field
    if password == password2:
      # check for username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'Username already taken')
        return redirect('register')
      else:
        # check for email
        if User.objects.filter(email=email).exists():
           messages.error(request, 'Email already taken')
           return redirect('register')
        else:
          # Looks good
          user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
          # Login after register
          # auth.login(request, user)
          # messages.success(request, 'You are now logged in')
          # return redirect('index')
          user.save()
          messages.success(request, 'You are now registered and can be log in')
          return redirect('login')
    else:
      messages.error(request, 'Password do not match')
      return redirect('register')

  else:
    return render(request, 'accounts/register.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are successfuly logout')
    return redirect('index')

def dashboard(request):
  contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
  content = {
    'contacts': contacts
  }
  return render(request, 'accounts/dashboard.html', content)