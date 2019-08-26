from django.shortcuts import render
import requests


def button(request):
    return render(request, 'home.html')

def output(request):
    data = requests.get('https://api.binance.com/api/v1/klines?symbol=BTCUSDT&interval=1m')
    print(data.text)
    data = data.text
    return render(request, 'home.html', {'data': data})

