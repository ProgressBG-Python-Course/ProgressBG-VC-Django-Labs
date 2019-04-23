from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms.models import model_to_dict


def index(request):
    return HttpResponse('OK')

