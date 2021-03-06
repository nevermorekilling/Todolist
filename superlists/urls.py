"""superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
# from django.contrib import admin
from lists import views as list_views
from lists import urls as list_urls
from accounts import views as account_views
from django.contrib.auth.views import logout

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', list_views.home_page, name='home'),
    # no / at the end of the url , means an action
    url(r'^lists/', include(list_urls)),
    url(r'^accounts/send_login_email',
        account_views.send_login_email,
        name='send_login_email'),
    url(r'^accounts/login', account_views.login, name='login'),
    url(r'^accounts/logout', logout, {'next_page': '/'}, name='logout'),
]
