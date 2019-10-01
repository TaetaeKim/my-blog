# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return HttpResponse('<h1>여기는 218230085 김태연 홈페이지!</h1>'
                        '<p>이전에 진행해본 프로젝트가 있어서 url을 변경하여(example/) 업로드하였습니다!</p>'
                        '<p>감사합니다. ^^</p>')