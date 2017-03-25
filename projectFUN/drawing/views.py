from django.core.files.base import ContentFile

import base64
from base64 import b64decode
from random import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from login_form.models import User
# Create your views here.


def enter_username(req):
    if req.method == 'GET':
        return render(req, 'login.html')
    elif req.method == 'POST':
        username = req.POST.get('username')
        req.session['username'] = username
        print(username)
        return redirect('/play')


def count_users(req):
    users = User.objects.filter(is_active=1)
    print('COUNT USERS')
    return JsonResponse({ 'users': users.count() })


def request_game(req):
    return render(req, 'waiting.html')


def play(req):
    # import ipdb; ipdb.set_trace();
    users = User.objects.filter(is_active=1)
    if req.method == 'GET':
        topic = take_topic()
        return render(req, 'room.html', locals())
    if req.method == 'POST':
        if 'user.jpeg' in req.POST:
            print('Pic')
            curr_user = User.objects.filter(email=req.session['email']).first()
            image_data = b64decode(req.POST['user.jpeg'])
            # prin(tcurr_user.username)
            curr_user.img = ContentFile(image_data, 'whatup.png')
            curr_user.save()
            img_data = req.POST['user.jpeg']
            img_data = img_data.split(',')[1]
            img_data = bytes(img_data, 'utf-8')
            print(type(img_data))
            with open('test.png', 'wb') as f:
                f.write(base64.decodebytes(img_data))
            # print('?????????????????')
            return redirect('/start_playing')  # Should redirect to the resultRoom
    return redirect('/start_playing')


def take_topic():
    with open('drawing/doodles.txt', 'r') as f:
        topics = eval(f.read());
    return topics[int(random() * len(topics))]

# def result_room(req):
#     if req.method == 'GET':
#         users = User.objects.filter(is_active=1)
#         return render(result_room)
