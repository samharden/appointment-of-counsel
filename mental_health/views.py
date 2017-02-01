from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .forms import *
from .templates import *



def index(request):

    indexform = MentalIndexForm(request.POST)

    if request.method == 'POST':
        print("Hello")
        indexform = MentalIndexForm(request.POST)

        if indexform.is_valid():
            print("Valid index")
            choice = indexform.cleaned_data['choice']
            print(choice)

            if choice == 'baker_act':

                return HttpResponseRedirect('baker-act.html')

            elif choice == 'marchman_act':

                return HttpResponseRedirect('marchman-act.html')

        else:
            indexform = MentalIndexForm()

    # if a GET (or any other method) we'll create a blank form
    else:
        indexform = MentalIndexForm()


    print("Top of index")


    return render(request, 'fl-mental-health/index.html', {'indexform': indexform})






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
