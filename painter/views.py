from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Painter

def painterView (request):
    all_painters = Painter.objects.all()
    return render(request, "painters.html",
    {"all_painters": all_painters})

def addPainter (request):
    p_firstname = request.POST['firstname']
    p_surname = request.POST['surname']
    p_country = request.POST['country']


    new_painter = Painter(firstname=p_firstname, surname=p_surname, country=p_country)
    new_painter.save()
    return HttpResponseRedirect('/painters/')

def deletePainter (request, painter_id):
    item = Painter.objects.get(id=painter_id)
    item.delete()
    return HttpResponseRedirect('/painters/')