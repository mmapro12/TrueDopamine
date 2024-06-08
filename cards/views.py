from django.shortcuts import render
from .models import Card

# Create your views here.
def home(request):
    islamiyat = Card.objects.filter(category="islamiyat").all()
    selfup = Card.objects.filter(category="self-up").all()
    sport = Card.objects.filter(category="sport").all()
    programming = Card.objects.filter(category="programming").all()
    montage = Card.objects.filter(category="montage").all()
    random = Card.objects.filter(category="random").all()
    language = Card.objects.filter(category="language").all()
    ai = Card.objects.filter(category="ai").all()

    context = {
        'islamiyat': islamiyat,
        'selfup': selfup,
        'sport': sport,
        'programming': programming,
        'montage': montage,
        'random':random,
        'language': language,
        'ai': ai,
    }

    return render(request, 'home.html', context=context)
