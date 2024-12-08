from django.shortcuts import render, redirect
from .models import Character
from .forms import CharacterForm
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

def character_list(request):
    characters = Character.objects.all()
    return render(request, 'game/character_list.html', {'characters': characters})

def add_character(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('character_list')
    else:
        form = CharacterForm()
    return render(request, 'game/add_character.html', {'form': form})

def search_characters(request):
    query = request.GET.get('q')
    characters = Character.objects.filter(name__icontains=query) if query else None
    return render(request, 'game/search_characters.html', {'characters': characters})

def homepage(request):
    current_datetime = datetime.now()
    return render(request, 'game/homepage.html', {'current_datetime': current_datetime})

from django.shortcuts import render, redirect
from .models import Character
from .forms import CharacterForm

def add_character(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('character_list')
    else:
        form = CharacterForm()
    return render(request, 'game/add_character.html', {'form': form})

def character_detail(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    return render(request, 'game/character_detail.html', {'character': character})

def send_test_email(request):
    if request.method == "POST":
        try:
            send_mail(
                'PROYECT QT',
                'ESTE UN JUEGO PARA ADULTOS',
                settings.EMAIL_HOST_USER,
                ['ronaldo.diazchacon@cesunbc.edu.mx'], 
                fail_silently=False,
            )
            return HttpResponse("Correo enviado exitosamente")
        except Exception as e:
            return HttpResponse(f"Error al enviar el correo: {e}")
    return render(request, 'game/send_email.html')



