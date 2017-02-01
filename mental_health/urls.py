from django.conf.urls import url
from . import views
from mental_health.view_routes import (
                                        marchman_act,
                                        baker_act,
                                    )

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^marchman-act.html$',
        marchman_act.marchman_act,
        name='marchman_act'),
    url(r'^baker-act.html$',
        baker_act.baker_act,
        name='baker_act'),
    ]
