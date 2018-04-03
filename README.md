# Django-Web3-Auth

django-web3-auth is a pluggable Django app that enables login/signup via an Ethereum wallet (a la CryptoKitties). The user authenticates themselves by digitally signing the session key with their wallet's private key.

## Installation

django-web3-auth has no releases yet, you'll need to install it from repository:
```bash
pip install https://github.com/atereshkin/django-web3-auth/archive/master.zip
```

You will also need [Web3.js](https://github.com/ethereum/web3.js) included in your pages.

## Usage

1. Add `'web3auth'` to the `INSTALLED_APPS` setting
2. Set `'web3auth.backend.Web3Backend'` as your authentication backend:
```python
AUTHENTICATION_BACKENDS = ['web3auth.backend.Web3Backend']
```
3. Bind some URLs to `web3auth.views.login_view` and `web3auth.views.signup_view`. Both views take an optional `template_name` argument. 
```python
from django.conf.urls import url

from web3auth import views as web3auth_views

urlpatterns = [
    url(r'^login/$', web3auth_views.login_view, {'template_name' : 'login.html'}, name='login'),
    url(r'^signup/$', web3auth_views.signup_view, name='signup'),
]

```
4. Code your templates for login and signup pages. Example code can be found in [login.html](web3auth/templates/web3auth/login.html) and [signup.html](web3auth/templates/web3auth/signup.html)
