from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting

"""
TODO:
- Create Course Info Dataframe (csv)
- Create Course Recommendations List
- Edit recommend function to serve recommendations
- Move Global Vars to external data file
"""

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

course_recommendations = {
    "thy" : ["CS 70", "CS 170"],
    "sys" : ["CS 162", "CS 161"],
    "mlai" : ["CS 189", "EECS 126"],
    "hci" : ["CS 160"]
    }

specialization_name_map = {
    "thy" : "theory",
    "mlai" : "ML/AI",
    "sys" : "systems",
    "hci" : "human-computer interaction"
    }

def recommend(request):
    #Input: request with user input.
    #Output: Recommendations page with class suggestions.
    specialization = request.POST['spec']
    print("CUSTOM LOG MSG. Requested: {}".format(specialization))
    recommendation_string = ', '.join(course_recommendations[specialization])
    new_context = {"spec":specialization_name_map[specialization],"recommendation":recommendation_string}
    return render(request, "recommendations.html", context=new_context)

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, "db.html", {"greetings": greetings})
