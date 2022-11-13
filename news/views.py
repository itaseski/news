from django.shortcuts import render
from django.http import HttpResponse

def index(require):
    return HttpResponse('Hello world')

def test(require):
    return HttpResponse('Test page')