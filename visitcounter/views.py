from django.shortcuts import render
from .models import Visit

def licznik_odwiedzin(request):
    licznik, created = Visit.objects.get_or_create(id=1)

    licznik.count += 1
    licznik.save()

    return render(request, 'visitcounter/index.html', {'visit_count': licznik.count})