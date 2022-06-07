from django.views.generic import ListView, DetailView
from django.shortcuts import render
from sports.models import Sporty


def index(request):
    sports = Sporty.objects.order_by('nazev_sportu')[:3]
    context={
        'sports': sports,
    }
    return render(request, 'index.html', context=context)


class sportListView(ListView):
    model=Sporty
    context_object_name = 'sporty'
    template_name = 'sporty.html'

class sportDetaily(DetailView):
    model =Sporty
    context_object_name = 'sporty_detail'
    template_name = 'detail.html'