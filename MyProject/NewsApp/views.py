from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import News, RegistrationData
from .forms import RegistrationForm, RegistrationModal
from django.contrib import messages


# Create your views here.

def Home(request):

  context = {
    "name":"Foivos",
    "number":"1st"
  }

  return render(request, 'home.html', context)

def About(request):
  return render(request, 'about.html')


def NewsViews(request):


  current = News.objects.order_by('pub_date')
  context = {'all': current}
  print(context)
  # first = News.objects.get(id=1)
  # second = News.objects.get(id=2)
  # context = {
  #   "data1": first,
  #   "data2": second
  # }
  # print(context)
  return render(request, 'news.html',context)

def NewsDate(request, year=2022):
  article_list = News.objects.filter(pub_date__year = year)

  context = {

    'year':year,
    'article_list': article_list
  }

  print(article_list)
  
  return render(request, 'newsdate.html', context)

def Contact(request):
  return render(request, 'contact.html')

def Register(request):

  context = {
    "form": RegistrationForm()

  }

  return render(request, 'signup.html',context)

def addUser(request):
  form = RegistrationForm(request.POST)

  if form.is_valid():
    myregister = RegistrationData(username= form.cleaned_data["username"],
    password= form.cleaned_data["password"],
    email= form.cleaned_data["email"],
    phone= form.cleaned_data["phone"]
    )

    myregister.save()
    messages.add_message(request, messages.SUCCESS, "You have signup succesccfully")

  return redirect('Registers')


def modalform(request):

  context =   {
    "modalform": RegistrationModal

  }


  return render(request, 'modalform.html',context)
  

def addmodalform(request):
  mymodalform = RegistrationModal(request.POST)

  if mymodalform.is_valid():
    mymodalform.save()

  return redirect('form')