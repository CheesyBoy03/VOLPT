from django.shortcuts import render
from .models import Day


def timetable_view(request):
    day = Day.objects.all()

    context = {'day': day}
    return render(request, 'timetable/timetable.html', context)
