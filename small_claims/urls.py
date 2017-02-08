from django.conf.urls import url
from . import views
from small_claims.view_routes import (
                                        sc_complaint,
                                    )

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^complaint-builder.html$',
        sc_complaint.sc_complaint,
        name='sc_complaint'),
    ]
