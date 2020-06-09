from django.shortcuts import render,  redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
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
    print("List :",lst)
    return render (request,"dashboard.html",{"lst":lst})



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
        
        
        print("###########","Name :",name, "title ;", title, "Radio :", multi)
    return render(request, "survey1.html", {"name": name, "title" : title, "multi":multi,"ques":ques})


def survey(request):
    if request.method == 'POST':
        if multi is 1:
            choice = request.POST['c1']+","+request.POST['c2']+","+request.POST['c3']+","+request.POST['c4']
        if multi is 0:
            choice = request.POST['c1']
        madinatory = request.POST['m']
        print("################","ques",ques,name)
        q=Survey(qtn = ques, name = name, title = title, multiple =  multi, choice = choice, mandatory = madinatory )
        q.save()
        print(choice,":",type(choice))

        return redirect (dashboard)