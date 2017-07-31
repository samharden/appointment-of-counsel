from django.conf.urls import url
from . import views
from appointment.view_routes import (
                                        appointment_view,
                                    )

urlpatterns = [

    url(r'^form$',
        appointment_view.form_fill,
        name='form-fill'),
    ]
