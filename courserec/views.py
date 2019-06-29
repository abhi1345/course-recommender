from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting
import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

"""
TODO:
- Create Course Info Dataframe (csv)
- Create Course Recommendations List
- Edit recommend function to serve recommendations
- Move Global Vars to external json file
"""
print("Directory path: {}".format(dir_path))
#Loading External Data

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def load_data():
    output_json = json.load(open('course_data.json'))
    specialization_name_map = output_json['specialization_name_map']
    course_recommendations = output_json['course_recommendations']
    return specialization_name_map, course_recommendations

def recommend(request):
    #Input: request with user input.
    #Output: Recommendations page with class suggestions.
    specialization = request.POST['spec']
    specialization_name_map, course_recommendations = load_data()
    print("CUSTOM LOG MSG. Requested: {}".format(specialization))
    recommendation_string = ', '.join(course_recommendations[specialization])
    new_context = {"spec":specialization_name_map[specialization],"recommendation":recommendation_string}
    return render(request, "recommendations.html", context=new_context)

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, "db.html", {"greetings": greetings})
