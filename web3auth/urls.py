from django.conf.urls import url

from web3auth import views

urlpatterns = [
    url(r'^demo/$', views.demo),
    url(r'^login/$', views.login_view),
    url(r'^signup/$', views.signup_view),

]
