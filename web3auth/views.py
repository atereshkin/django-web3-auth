import random
import string

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.conf import settings

from web3auth.forms import LoginForm, SignupForm
from web3auth.utils import recover_to_addr

def demo(request):
    return render(request,
                  'web3auth/demo.html',
                  {})
                  

def login_view(request, template_name='web3auth/login.html'):
    if request.method == 'POST':
        token = request.session['login_token']
        form = LoginForm(token, request.POST)
        if form.is_valid():
            if form.user is not None:
                del request.session['login_token']
                login(request, form.user)                
                return redirect(request.GET.get('next') or request.POST.get('next') or settings.LOGIN_REDIRECT_URL)
            else:
                request.session['ethereum_address'] = recover_to_addr(token, form.cleaned_data['signature'])
                return redirect(signup_view)
    else:
        token = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(32))
        request.session['login_token'] = token
        form = LoginForm(token)
    return render(request,
                  template_name,
                  {'form' : form,
                   'login_token' : token})


def signup_view(request, template_name='web3auth/signup.html'):
    ethereum_address = request.session['ethereum_address']
    if request.method == 'POST':        
        form = SignupForm(request.POST)
        if form.is_valid():
            del request.session['ethereum_address']
            user = form.save(commit=False)
            user.username = ethereum_address
            user.save()            
            login(request, user)                
            return redirect(request.GET.get('next') or request.POST.get('next') or settings.LOGIN_REDIRECT_URL)
    else:
        form = SignupForm()
    return render(request,
                  template_name,
                  {'form' : form})
    
