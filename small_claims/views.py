from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .forms import *
from .templates import *



def index(request):

    indexform = SmallClaimsIndexForm(request.POST)

    if request.method == 'POST':
        print("Hello")
        indexform = SmallClaimsIndexForm(request.POST)

        if indexform.is_valid():
            print("Valid index")
            choice = indexform.cleaned_data['choice']
            print(choice)

            if choice == 'complaint':

                return HttpResponseRedirect('complaint-choices.html')

            elif choice == 'marchman_act':

                return HttpResponseRedirect('marchman-act.html')

        else:
            indexform = SmallClaimsIndexForm()

    # if a GET (or any other method) we'll create a blank form
    else:
        indexform = SmallClaimsIndexForm()


    print("Top of index")


    return render(request, 'fl-small-claims/index.html',  {'indexform': indexform})

def complaint_choices(request):

    choicesform = SmallClaimsComplaintChoiceForm(request.POST)

    if request.method == 'POST':
        print("Hello")
        choicesform = SmallClaimsComplaintChoiceForm(request.POST)

        if choicesform.is_valid():
            print("Valid index")
            choice = choicesform.cleaned_data['choice']
            print(choice)

            if choice == 'nonauto':

                return HttpResponseRedirect('small-claims-complaint.html')

            elif choice == 'auto':

                return HttpResponseRedirect('auto-complaint-choices.html')

        else:
            choicesform = SmallClaimsComplaintChoiceForm()

    # if a GET (or any other method) we'll create a blank form
    else:
        choicesform = SmallClaimsComplaintChoiceForm()


    print("Top of index")


    return render(request, 'fl-small-claims/complaint-choices.html',  {'choicesform': choicesform})

def complaint_choices_auto(request):

    choicesform = SmallClaimsAutoComplaintChoiceForm(request.POST)

    if request.method == 'POST':
        print("Hello")
        choicesform = SmallClaimsAutoComplaintChoiceForm(request.POST)

        if choicesform.is_valid():
            print("Valid index")
            choice = choicesform.cleaned_data['choice']
            print(choice)

            if choice == 'Yes':

                return HttpResponseRedirect('small-claim-auto-md.html')

            elif choice == 'No':

                return HttpResponseRedirect('small-claim-auto.html')

        else:
            choicesform = SmallClaimsAutoComplaintChoiceForm()

    # if a GET (or any other method) we'll create a blank form
    else:
        choicesform = SmallClaimsAutoComplaintChoiceForm()


    print("Top of index")


    return render(request, 'fl-small-claims/auto-complaint-choices.html',  {'choicesform': choicesform})


def sitemap():
    return render_template('sitemap.xml')


def stylesheet():
    return render_template('stylesheet.css')

def text_info():
    return render_template('confirm_text_info.html')


def not_found_error(error):
    return render_template('404.html'), 404

def internal_error(error):
    #db.session.rollback()
    return render_template('500.html'), 500
