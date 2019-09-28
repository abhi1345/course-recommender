from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting
from .models import Row
import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

print("Directory path: {}".format(dir_path))
#Loading External Data

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def load_data():
    output_json = json.load(open('/app/courserec/course_data.json'))
    specialization_name_map = output_json['specialization_name_map']
    course_recommendations = output_json['course_recommendations']
    course_descriptions = output_json['course_descriptions']
    course_difficulties = output_json['course_difficulties']
    ret = (specialization_name_map, course_recommendations, course_descriptions, course_difficulties)
    return ret

def recommend(request):
    #Input: request with user input.
    #Output: Recommendations page with class suggestions.
    specialization = request.POST['spec']
    specialization_name_map, course_recommendations, course_descriptions, course_difficulties = load_data()
    person_list = []
    for course in course_recommendations[specialization]:
        course_difficulty = "Medium"
        for diff in ["Easy", "Medium", "Hard"]:
            if course in course_difficulties[diff]:
                course_difficulty = diff
        person = Row(name=course, description=course_descriptions[course], difficulty=course_difficulty)
        person_list.append(person)

    print("CUSTOM LOG MSG. Requested: {}".format(specialization))
    new_context = {"spec" : specialization_name_map[specialization], "recommendation" : person_list}
    return render(request, "recommendations.html", context=new_context)

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, "db.html", {"greetings": greetings})
