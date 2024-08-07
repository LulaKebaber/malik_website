from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout


def mainPage(request):
    page = 'main'
    context = {'page': page}

    return render(request, 'base/main_page.html', context)