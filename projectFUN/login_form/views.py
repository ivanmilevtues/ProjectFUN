from django.shortcuts import render, redirect

from login_form.forms import RegisterForm, LoginForm
from login_form.decorators import login_required, annon_required
from login_form.models import User


# Create your views here.
@annon_required(redirect_url='/play')
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['email'] = request.POST['email']
            return redirect('/play')
    form = RegisterForm()
    return render(request, 'register.html', locals())


@annon_required(redirect_url='/play')
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.find()
            if u:
                request.session['email'] = request.POST['email']
                return redirect('/play')
    form = LoginForm()
    return render(request, 'sign_in.html', locals())


@login_required(redirect_url='/login')
def profile(request):
    if request.method == 'GET':
        u = User.objects.filter(email=request.session['email']).first()
    return render(request, 'profile.html', locals())
