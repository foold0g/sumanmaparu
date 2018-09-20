from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("Resume - Suman Maparu")

def bio(request, f_name):
  return HttpResponse("You're viewing the resume of %s" % f_name)

