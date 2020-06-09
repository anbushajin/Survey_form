from django.shortcuts import render,  redirect
from django.http import HttpResponse
from .models import *

ques=0
name=0
title=0
multi=0

def dashboard (request):
    lst=[]
    dict={}
    obj=Survey.objects.all()
    for i in obj:
        dict = {"qtn" : i.qtn, "name" : i.name, "title" : i.title, "multiple" :  i.multiple, "choice" : i.choice, "mandatory" : i.mandatory}
        lst.append(dict)
    return render (request,"dashboard.html",{"lst":lst})

def addquestion(request):
    if request.method == 'GET':
        return render (request, "question.html")
    elif request.method == 'POST':
        question = request.POST['q']
        ques = Question (question = question)
        ques.save()
        return redirect (dashboard)





def home(request):
    if request.method == 'GET':
        qstn= Question.objects.all()
        return render (request,"home.html",{"qstn":qstn})
    elif request.method == 'POST':
        global ques
        ques= request.POST['qty']
        return render (request, "survey.html", {"ques":ques})



def question(request):
    if request.method == 'POST':
        global name, title, multi
        name = request.POST['name']
        title= request.POST['title']
        multi= int(request.POST['radio'])
    return render(request, "survey1.html", {"name": name, "title" : title, "multi":multi,"ques":ques})


def survey(request):
    if request.method == 'POST':
        if multi is 1:
            choice = request.POST['c1']+","+request.POST['c2']+","+request.POST['c3']+","+request.POST['c4']
        if multi is 0:
            choice = request.POST['c1']
        madinatory = request.POST['m']
        q=Survey(qtn = ques, name = name, title = title, multiple =  multi, choice = choice, mandatory = madinatory )
        q.save()
        print(choice,":",type(choice))
        return redirect (dashboard)