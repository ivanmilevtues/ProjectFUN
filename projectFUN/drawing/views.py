from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.


def enter_username(req):
    if req.method == 'GET':
        return render(req, 'login.html')
    elif req.method == 'POST':
        username = req.POST.get('username')
        req.session['username'] = username
        print(username)
        return redirect('/play')


def play(req):
    # import ipdb; ipdb.set_trace();
    if req.method == 'GET':
        uname = req.session.get('username')
        return render(req, 'room.html', locals())
    if req.method == 'POST':
        if 'user.jpeg' in req.POST:
            print('Here is img')
            return HttpResponse('success')
    return HttpResponse('FAIL!!!!!')
