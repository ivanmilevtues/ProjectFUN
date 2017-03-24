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
    # if req.method == 'GET':
    uname = req.session.get('username')
    return render(req, 'room.html', locals())
