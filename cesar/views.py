from django.shortcuts import render
from django.http import HttpResponse
import json

from cesar.cesar_сrypt import shifr, freq_analysis, info_decrypt


def crypt(request):
    """
    Шифровка введенного сообщения
    """
    data = {
        'crypt_text': 'Finland',
    }
    if request.is_ajax():
        if request.method == 'GET':
            input_text = request.GET['text']
            rot = int(request.GET['rot'])
            crypt_text = shifr(input_text, rot)
            data['crypt_text'] = crypt_text

    json_date = json.dumps(data)
    return HttpResponse(json_date, content_type='application/json')


def decrypt(request):
    """
    Дешифровка введенного сообщения
    """
    data = {
        'info_decrypt': 'Finland',
    }
    if request.is_ajax():
        if request.method == 'GET':
            input_text = request.GET['text']
            rot = -int(request.GET['rot'])
            info_decrypt = shifr(input_text, rot)
            data['info_decrypt'] = info_decrypt

    json_date = json.dumps(data)
    return HttpResponse(json_date, content_type='application/json')


def analysis(request):
    """
    Анализирует вводимый текст, выводит частотную диаграмму и предположительную шифровку
    """
    data = {
        'text': 'Finland',
        'freq': dict
    }

    if request.is_ajax():
        if request.method == 'GET':
            input_text = request.GET['original_text']
            data['text'] = info_decrypt(input_text)
            data['freq'] = freq_analysis(input_text)

    json_date = json.dumps(data)
    return HttpResponse(json_date, content_type='application/json')


def index(request):
    return render(request, 'HTML/index.html')
