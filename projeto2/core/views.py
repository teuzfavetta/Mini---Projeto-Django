from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime



data = datetime.today()
TrueOrFalse = True or False

if data.day == 25 and data.month == 12:
    TrueOrFalse = True
else: 
    TrueOrFalse = False
            
def natal(request):     
    contexto = {
        'natal': TrueOrFalse
    }
    return render(request, 'natal.html', contexto)



if data.day == 21 and data.month == 4:
    TrueOrFalse = True
else: 
    TrueOrFalse = False
    
def tiradentes(request):
    contexto = {
        'tiradentes': TrueOrFalse
    }
    return render(request, 'tiradentes.html', contexto)

