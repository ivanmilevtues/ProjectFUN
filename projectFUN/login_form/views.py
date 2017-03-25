from django.shortcuts import render, redirect

from login_form.forms import RegisterForm


# Create your views here.
# @annon_required(redirect_url='/profile')
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['email'] = request.POST['email']
            return redirect('/profile')
    elif request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', locals())



def login(req):
    pass


def profile(req):
    pass
