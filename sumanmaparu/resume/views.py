from django.shortcuts import render
from .models import Person, Contact

# Create your views here.
def index(request):
    person = Person.objects.get(id=1)
    first_name = person.first_name
    last_name = person.last_name
    company = person.company
    profile_image = person.profile_image.url
    profile_description = person.profile_description

    contact = Contact.objects.get(id=1)
    email = contact.email
    phone = contact.phone
    house_number = contact.house_number
    street = contact.street
    area = contact.area
    city = contact.city
    county = contact.county
    post_code = contact.post_code
    country = contact.country
    #template = loader.get_template('resume/index.html')

    context = {
        'first_name': first_name,
        'last_name': last_name,
        'company': company,
        'profile_image': profile_image,
        'profile_description': profile_description,
        'email': email,
        'phone': phone,
        'house_number': house_number,
        'street': street,
        'area': area,
        'city': city,
        'county': county,
        'post_code': post_code,
        'country': country,
    }
    return render(request, 'resume/index.html', context)
