

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from main.forms import LoginForm, ProblemForm
from crim import templates
#


def home_page(request):
    # if this is a POST request we need to process the form data

    if request.method == 'POST':
        print("Hello")
        form = LoginForm(request.POST)

        if form.is_valid():
            print("Valid")
            name = form.cleaned_data['name']
            print(name)
            password = form.cleaned_data['password']
            print(password)
            if name == 'samharden' and password == 'hello':
                print('logged in')
                return HttpResponseRedirect('main/detail.html')
            else:
                form = LoginForm()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'main/home.html', {'form': form})


def search_page(request):
    # if this is a POST request we need to process the form data
    form = ProblemForm(request.POST)
    if request.method == 'POST':
        print("Hello")
        form = ProblemForm(request.POST)

        if form.is_valid():
            print("Valid")
            case_type = form.cleaned_data['case_type']
            print(case_type)
            if case_type == 'crim':

                return HttpResponseRedirect('/crim')
            elif case_type == 'discrim':
                return HttpResponseRedirect('/fl-discrim-helper')
        else:
            form = ProblemForm()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProblemForm()

    return render(request, 'main/detail.html', {'form': form})


def about(request):
    return render(request, 'main/about.html')

def disclaimer(request):
    return render(request, 'main/disclaimer.html')


def contact(request):
    return render(request, 'main/contact.html')
