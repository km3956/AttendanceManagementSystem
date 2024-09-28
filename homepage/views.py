from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class HomePageView(TemplateView):
    template_name = "homepage.html"


def homepage(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    else:
        if request.method == 'post':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('class-select')
            else:
                messages.info(request, 'Username OR Password is incorrect')

        context = {}
        return render(request, 'templates/homepage.html', context)
