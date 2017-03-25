from django.core.files.base import ContentFile
from base64 import b64decode

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
    if users.count() < 3:
        return JsonResponse({ 'users': users.count() })
    else:
        return redirect('/start_playing')


def request_game(req):
    return render(req, 'waiting.html')


def play(req):
    # import ipdb; ipdb.set_trace();
    users = User.objects.filter(is_active=1)
    if req.method == 'GET':
        return render(req, 'room.html', locals())
    if req.method == 'POST':
        if 'user.jpeg' in req.POST:
            print('Pic')
            curr_user = User.objects.filter(email=req.session['email']).first()
            image_data = b64decode(req.POST['user.jpeg'])
            print(curr_user.username)
            curr_user.img = ContentFile(image_data, 'whatup.png')
            curr_user.save()
            return redirect('/play')  # Should redirect to the resultRoom
    return HttpResponse('FAIL!!!!!')


# def result_room(req):
#     if req.method == 'GET':
#         users = User.objects.filter(is_active=1)
#         return render(result_room)
