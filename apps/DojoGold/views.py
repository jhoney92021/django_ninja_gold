from django.shortcuts import render, HttpResponse, redirect
from .models import *
import random, datetime

placeDict={
'Farm' : {'floor':10,'ceiling': 12},
'Cave' : {'floor':5, 'ceiling':10},
'House' : {'floor':2, 'ceiling':5},
'Casino' : {'floor':-50, 'ceiling':50}
}

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0 
    if 'text_color' not in request.session:
        request.session['text_color'] = 'blue' 
    

    context = {
        'gold': ledger.gold,
        'transactions': ledger.logNumber,
        'text_color': request.session['text_color'],
        'activities' : ledger.activitiesDict, 
        'reset': 'submit'
    }
    return render(request, 'DojoGold/index.html', context)

def process(request):
    request.session['workplace'] = request.POST['workplace']
    if request.session['workplace'] == 'Reset':
        ledger.clear() 
        request.session['text_color'] = 'blue' 
        return redirect('/')
    workInstant = request.session['workplace']
    workInstance = workplace(workInstant, placeDict[workInstant]['floor'], placeDict[workInstant]['ceiling'])
    print('*'*50,'\n','processing','\n','*'*50 )
    earnedToday = workInstance.earnGold()
    ledger.gold += earnedToday
    workInstance.log().endGame()
    request.session['text_color'] = str(workInstance.color)

    return redirect('/')