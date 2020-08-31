from django.shortcuts import render, redirect
from SearchEngine.search import google,yahoo,duck,ecosia


def homepage(request):
    return render(request,'home.html')


def results(request):
    if request.method == "POST":
        result = request.POST.get('search')
        google_link,google_text = google(result)
        google_data = zip(google_link,google_text)
        yahoo_link,yahoo_text = yahoo(result)
        yahoo_data = zip(yahoo_link,yahoo_text)
        duck_link,duck_text = duck(result)
        duck_data = zip(duck_link,duck_text)
        ecosia_link,ecosia_text = ecosia(result)
        ecosia_data = zip(ecosia_link,ecosia_text)
        if result == '':
            return redirect('Home')
        else:
            return render(request,'results.html',{'google': google_data, 'yahoo': yahoo_data, 'duck': duck_data, 'ecosia': ecosia_data})