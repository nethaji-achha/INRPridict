from django.http import HttpResponse
from django.shortcuts import render
import pickle
import numpy as np

# Create your views here.
prediction = 0
def index(request):
    return render(request, 'home.html')
    
def getpredictions(cny, pkl, lkr, amd, btd, btn, cve, xof, aoa, vall):
    # Load the model from the pickle file
    model = pickle.load(open('CRPRED.pkl', 'rb'))    
    # Make the prediction []
    array = [pkl, cny, lkr,  vall,  aoa, amd,  btd,  xof,  btn, cve]
    array = np.array(array).reshape(1, -1)
    prediction = model.predict(array)
    # prediction array
    prediction = np.array(prediction) 
    return prediction


def predict(request):
    if request.method == 'POST' :
        cny = request.POST.get('cny')
        pkl = request.POST.get('pkl')
        lkr = request.POST.get('lkr')
        amd = request.POST.get('amd')
        btd = request.POST.get('btd')
        btn = request.POST.get('btn')
        cve = request.POST.get('cve')
        xof = request.POST.get('xof')
        aoa = request.POST.get('aoa')
        vall = request.POST.get('all')
        crncy = {
            'cny': cny,
            'pkl': pkl,
            'lkr': lkr,
            'amd': amd,
            'btd': btd,
            'btn': btn,
            'cve': cve,
            'xof': xof,
            'aoa': aoa,
            'vall': vall,
        }
        INRprediction = getpredictions(cny, pkl, lkr, amd, btd, btn, cve, xof, aoa, vall)
    return render(request, 'result.html', {'crncy': crncy ,'INRprediction': INRprediction})
    