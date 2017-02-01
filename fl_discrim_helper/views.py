from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Question
from django.http import Http404

from .forms import *
# from flask.ext.login import login_user, logout_user, current_user, login_required


def index(request):

    indexform = DiscrimIndexForm(request.POST)

    if request.method == 'POST':
        print("Hello")
        indexform = DiscrimIndexForm(request.POST)

        if indexform.is_valid():
            print("Valid index")
            choice = indexform.cleaned_data['choice']
            print(choice)

            if choice == 'complaint':

                return HttpResponseRedirect('choose-complaint-type.html')

            elif choice == 'research':

                return HttpResponse('Search')

        else:
            indexform = DiscrimIndexForm()

    # if a GET (or any other method) we'll create a blank form
    else:
        indexform = DiscrimIndexForm()


    print("Top of index")


    return render(request, 'fl-discrim-helper/index.html', {'indexform': indexform})


def search():
    form = searchform()
    session['searchall'] = form.searchall._value()

    searchall = session['searchall']


    return render_template('search.html',
                           title='FCHR Opinion Search.html',
                           form=form
                           )

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
