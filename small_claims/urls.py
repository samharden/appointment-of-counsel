from django.conf.urls import url
from . import views
from small_claims.view_routes import (
                                        sc_complaint,
                                        sc_complaint_auto,
                                        sc_complaint_auto_md,
                                    )

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^complaint-choices.html', views.complaint_choices, name='complaint-choices'),
    url(r'^auto-complaint-choices.html', views.complaint_choices_auto, name='complaint-choices-auto'),
    url(r'^small-claims-complaint.html$',
        sc_complaint.sc_complaint,
        name='sc_complaint'),
    url(r'^small-claim-auto.html$',
        sc_complaint_auto.sc_complaint_auto,
        name='sc_complaint_auto'),
    url(r'^small-claim-auto-md.html$',
        sc_complaint_auto_md.sc_complaint_auto_md,
        name='sc_complaint_auto'),
    ]
