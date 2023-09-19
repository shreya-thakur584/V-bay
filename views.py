# registration/views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup_success')  # You can define this URL later
    else:
        form = RegistrationForm()
    
    return render(request, 'registration/signup.html', {'form': form})
