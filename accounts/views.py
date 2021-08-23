# import sys
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages, auth
from accounts.models import Token
from django.core.urlresolvers import reverse


def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    # print(reverse('login'))
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid)
    )
    # print(url)
    message_body = f'Use this link to log in:\n\n{url}'
    send_mail(
        'Your login link for Superlists',
        message_body,
        'noreply@superlists',
        [email])
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in.")
    return redirect('/')


def login(request):
    # print('login view', file=sys.stderr)
    token = request.GET.get('token')
    # uid = request.GET.get('token')

    user = auth.authenticate(uid=token)
    # user = auth.authenticate(uid=uid)
    if user is not None:
        auth.login(request, user)
    return redirect('/')
