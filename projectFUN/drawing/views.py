from django.shortcuts import render

# Create your views here.


def enter_username(req):
    if req.method == 'GET':
        return render(req, 'login.html')
    elif req.method == 'POST':
        username = req.POST.get('username')
        print(username)
        return render(req, 'room.html')
