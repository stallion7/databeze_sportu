from django.shortcuts import render
from sports.models import Sporty


def index(request):
    sports = Sporty.objects.order_by('nazev_sportu')[:3]
    context={
        'sports': sports,
    }
    return render(request, 'index.html', context=context)
