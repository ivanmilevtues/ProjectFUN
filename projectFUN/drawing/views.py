from django.core.files.base import ContentFile

import base64
from base64 import b64decode
from random import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from login_form.models import User
# Create your views here.


def count_users(req):
    users = User.objects.filter(is_active=1)
    return JsonResponse({ 'users': users.count() })


def request_game(req):
    return render(req, 'waiting.html')


def play(req):
    # import ipdb; ipdb.set_trace();
    users = User.objects.filter(is_active=1)
    if req.method == 'GET':
        topic = take_topic()
        user = User.objects.filter(email=req.session['email']).first()
        return render(req, 'room.html', locals())
    if req.method == 'POST':
        if 'user.jpeg' in req.POST:
            try:
                curr_user = User.objects.filter(email=req.session['email']).first()
                # filename = 'drawing/static/drawing/images/img_' + req.session.get('email') + '.png';
                # curr_user.img = filename
                # curr_user.save()
                # img_data = req.POST['user.jpeg']
                # img_data = img_data.split(',')[1]
                # img_data = bytes(img_data, 'utf-8')

                # print('?')
                # with open(filename, 'wb') as f:
                #     f.write(base64.decodebytes(img_data))
                # print('File saved in:', filename)
                # image_data = b64decode(req.POST['user.jpeg'])
                # prin(tcurr_user.username)
                curr_user.img = req.POST['user.jpeg']
                curr_user.save()
                print(req.POST['user.jpeg'])
                curr_user = User.objects.filter(email=req.session['email']).first()
            except:
                print('Error')
            finally:
                # if not curr_user.is_king:
                #     sleep(2)
                return redirect('/result_room')  # Should redirect to the resultRoom
    return redirect('/start_playing')


def final_room(req):
    users = User.objects.filter(is_active=1) 
    curr_user = User.objects.filter(email=req.session['email']).first()
    print(users)
    return render(req, 'final_room.html', locals())


def take_topic():
    with open('drawing/doodles.txt', 'r') as f:
        topics = eval(f.read());
    return topics[1]
