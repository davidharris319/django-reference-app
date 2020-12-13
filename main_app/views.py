from django.shortcuts import render
from django.http import HttpResponse


class Dog:  # Note that parens are optional if not inheriting from another class
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age


dogs = [
    Dog('Madison', 'yellow lab', 'young pupper', 3),
    Dog('Casey', 'black lab', 'old puper', 15),
    Dog('Raven', 'mixed-breed', 'lazy pupper', 10)
]

# Create your views here.


def home(request):
    return HttpResponse('<h1> Hello 🐶 </h1>')


def about(request):
    return render(request, 'about.html')


def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})
