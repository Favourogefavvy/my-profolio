from pathlib import Path
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.templatetags.static import static
from .forms import ContactForm
from .models import Skill

# Create your views here.

#Homepage
def home(request):
    profile_image_path = Path(settings.BASE_DIR) / 'static' / 'images' / 'profile.jpg'
    profile_image_url = static('images/profile.jpg')
    if profile_image_path.exists():
        profile_image_url = f"{profile_image_url}?v={int(profile_image_path.stat().st_mtime)}"
    return render(request, 'portfolio/home.html', {'profile_image_url': profile_image_url})

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

# about page
def about(request):
    return render(request, 'portfolio/about.html')