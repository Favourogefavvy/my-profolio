from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Skill

# Create your views here.

#Homepage
def home(request):
    return render(request, 'portfolio/home.html')

#skills page
def skills(request):
    all_skills = Skill.objects.all()
    return render(request, 'portfolio/skills.html', {'skills': all_skills})

#contact page
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})