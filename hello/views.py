from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def about(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index2.html")

test_dict = {"specialization":"Machine Learning / Artificial Intelligence"}

def recommend(request):
    data= request.POST.get('data','')
    print("CUSTOM LOG MSG")
    print(data)
    print(request)
    print(request.POST)
    print(request.POST['spec'])
    return render(request, "index3.html", context=test_dict)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
