from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def about(request):
    return render(request, "index2.html")

test_dict = {"specialization":"Machine Learning / Artificial Intelligence"}

course_recommendations = {
    "thy" : ["CS 70"],
    "sys" : ["CS 162"],
    "mlai" : ["CS 189"],
    "hci" : ["CS 160"]
    }

spec_names = {
    "thy" : "theory",
    "mlai" : "ML/AI",
    "sys" : "systems",
    "hci" : "human-computer interaction"
    }

"""
TODO:
- Create Course Info Dataframe (csv)
- Create Course Recommendations List
- Edit recommend function to serve recommendations
- Move Global Vars to external data file
"""


def recommend(request):
    #String abbreviation of specialization
    spec = request.POST['spec']
    print("CUSTOM LOG MSG. Requested: {}".format(spec))

    #Dictionary with spec = full name of specialization
    new_context = {"spec" : spec_names[spec], "test" : "Hello /n var"}

    return render(request, "index3.html", context=new_context)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
