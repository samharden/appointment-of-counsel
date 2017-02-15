
"""
idea: person facing small claims case inputs their name or case number and
the app uses selenium / phantomJS to go scrape the court docket info (judge,
defendant, upcoming court dates, etc.) then asks questions based on case type,
i.e. "Did the accident happen in Hillsborough County?" "Were you driving the
car?" "Was an accident report filed?"
Then the system puts out a report on the past five years of data for that judge:
do cases typically settle in mediation? What happens if they go to trial? Do I do
better with a lawyer vs. without?
"""

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from small_claims.form_folder.find_case import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import StringIO, BytesIO
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch


def sc_defendant(request):

    case_info = CaseInfo(request)



    if request.method == 'POST':

        case_info = CaseInfo(request.POST)

        if case_info.is_valid():
            print("Valid")

            county = request.POST.get('county')
            party_name = request.POST.get('party_name')
            case_number = request.POST.get('case_number')


    else:
        case_info = CaseInfo()

    return render(request,'fl-small-claims/find-case.html',
                    {'case_info': case_info})


def search_for_case(county, party_name, case_number):
    pass
