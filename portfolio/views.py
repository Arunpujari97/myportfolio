from django.shortcuts import render, redirect
from .forms import RecruiterForm
from .models import Recruiter

def ask_user_type(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        request.session['user_type'] = user_type
        if user_type == 'recruiter':
            return redirect('recruiter_form')
        else:
            return redirect('home')
    return render(request, 'portfolio/ask_user_type.html')

def recruiter_form(request):
    if request.method == 'POST':
        form = RecruiterForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['is_recruiter'] = True
            return redirect('home')
    else:
        form = RecruiterForm()
    return render(request, 'portfolio/recruiter_form.html', {'form': form})

def home(request):
    is_recruiter = request.session.get('is_recruiter', False)
    return render(request, 'portfolio/home.html', {'is_recruiter': is_recruiter})
