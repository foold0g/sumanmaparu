from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Person

# Create your views here.
def index(request):
  person = Person.objects.get(id=1)
  first_name = person.first_name
  last_name = person.last_name
  company = person.company
  profile_image = person.profile_image.url
  #template = loader.get_template('resume/index.html')

  context = {
    'first_name': first_name,
    'last_name': last_name,
    'company': company,
    'profile_image': profile_image
  }
  return render(request, 'resume/index.html', context)

def bio(request):
  context = {
    'first_name': first_name,
  }
  return render(request, 'resume/index.html', context)
