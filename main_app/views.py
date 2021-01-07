from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Dog, Toy
from .forms import FeedingForm

# Create your views here.


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@login_required
def dogs_index(request):
    dogs = Dog.objects.filter(user=request.user)
    return render(request, 'dogs/index.html', {'dogs': dogs})


@login_required
def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    toys_cat_doesnt_have = Toy.objects.exclude(
        id__in=dog.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'dogs/detail.html', {
        'dog': dog, 'feeding_form': feeding_form, 'toys': toys_cat_doesnt_have
    })


class DogCreate(LoginRequiredMixin, CreateView):
    model = Dog
    fields = ['name', 'breed', 'description', 'age']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DogUpdate(LoginRequiredMixin, UpdateView):
    model = Dog
    fields = ['breed', 'description', 'age']


class DogDelete(LoginRequiredMixin, DeleteView):
    model = Dog
    success_url = '/dogs/'


@login_required
def add_feeding(request, dog_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # Validate the form
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.dog_id = dog_id
        new_feeding.save()
    return redirect('detail', dog_id=dog_id)


class ToyList(LoginRequiredMixin, ListView):
    model = Toy


class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields = '__all__'


class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = ['color']


class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    success_url = '/toys/'


class ToyDetail(LoginRequiredMixin, DetailView):
    model = Toy


@login_required
def assoc_toy(request, dog_id, toy_id):
    Dog.objects.get(id=dog_id).toys.add(toy_id)
    return redirect('detail', dog_id=dog_id)
