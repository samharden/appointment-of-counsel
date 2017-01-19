from django.conf.urls import url
from . import views
from fl_discrim_helper.view_routes import (
                                    choose_complaint_type,
                                    pub_acc_complaint,
                                    )

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),

    url(r'^choose-complaint-type.html$',
        choose_complaint_type.choose_complaint_type,
        name='choose-complaint-type'),

    url(r'^pub-acc-complaint.html$',
        pub_acc_complaint.pub_acc_complaint,
        name='pub-acc-complaint'),

]
