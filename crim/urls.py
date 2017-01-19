from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views
from crim.view_routes.hills import (hillsborough_dwlsr,
                                    hillsborough_dui,
                                    hillsborough_battery,
                                    hillsborough_petit_theft,
                                    hillsborough_marijuanaposs,
                                    )
from crim.view_routes.pinel import (pinellas_dui,
                                    pinellas_marijuanaposs,
                                    pinellas_battery,
                                    pinellas_dwlsr,
                                    pinellas_petit_theft,

                                    )


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^fl/hills/hillsborough-dui.html$',
        hillsborough_dui.hillsborough_dui,
        name='hillsborough-dui'),

    url(r'^fl/hills/dui/dui.html$',
        hillsborough_dui.dui,
        name='hills-dui-dui'),

    url(r'^fl/hills/dui/farrdui.html$',
        hillsborough_dui.farr,
        name='hills-dui-farr'),

    url(r'^fl/hills/dui/grecodui.html$',
        hillsborough_dui.greco,
        name='hills-dui-greco'),

    url(r'^fl/hills/dui/jeskedui.html$',
        hillsborough_dui.jeske,
        name='hills-dui-jeske'),

    url(r'^fl/hills/dui/leflerdui.html$',
        hillsborough_dui.lefler,
        name='hills-dui-lefler'),

    url(r'^fl/hills/dui/mcneildui.html$',
        hillsborough_dui.mcneil,
        name='hills-dui-mcneil'),

    url(r'^fl/hills/dui/myersdui.html$',
        hillsborough_dui.myers,
        name='hills-dui-myers'),

    url(r'^fl/hills/dui/taylordui.html$',
        hillsborough_dui.taylor,
        name='hills-dui-taylor'),

    url(r'^fl/hills/battery/battery.html$',
        hillsborough_battery.battery,
        name='hills-battery-battery'),

    url(r'^fl/hills/battery/farrbattery.html$',
        hillsborough_battery.farr,
        name='hills-battery-farr'),

    url(r'^fl/hills/battery/grecobattery.html$',
        hillsborough_battery.greco,
        name='hills-battery-greco'),

    url(r'^fl/hills/battery/jeskebattery.html$',
        hillsborough_battery.jeske,
        name='hills-battery-jeske'),

    url(r'^fl/hills/battery/leflerbattery.html$',
        hillsborough_battery.lefler,
        name='hills-battery-lefler'),

    url(r'^fl/hills/battery/mcneilbattery.html$',
        hillsborough_battery.mcneil,
        name='hills-battery-mcneil'),

    url(r'^fl/hills/battery/myersbattery.html$',
        hillsborough_battery.myers,
        name='hills-battery-myers'),

    url(r'^fl/hills/battery/taylorbattery.html$',
        hillsborough_battery.taylor,
        name='hills-battery-taylor'),


    url(r'^fl/hills/dwlsr/dwlsr.html$',
        hillsborough_dwlsr.dwlsr,
        name='hills-dwlsr-dwlsr'),

    url(r'^fl/hills/dwlsr/farr.html$',
        hillsborough_dwlsr.farr,
        name='hills-dwlsr-farr'),

    url(r'^fl/hills/dwlsr/greco.html$',
        hillsborough_dwlsr.greco,
        name='hills-dwlsr-greco'),

    url(r'^fl/hills/dwlsr/jeske.html$',
        hillsborough_dwlsr.jeske,
        name='hills-dwlsr-jeske'),

    url(r'^fl/hills/dwlsr/lefler.html$',
        hillsborough_dwlsr.lefler,
        name='hills-dwlsr-lefler'),

    url(r'^fl/hills/dwlsr/mcneil.html$',
        hillsborough_dwlsr.mcneil,
        name='hills-dwlsr-mcneil'),

    url(r'^fl/hills/dwlsr/myers.html$',
        hillsborough_dwlsr.myers,
        name='hills-dwlsr-myers'),

    url(r'^fl/hills/dwlsr/taylor.html$',
        hillsborough_dwlsr.taylor,
        name='hills-dwlsr-taylor'),

    url(r'^fl/hills/marijuana-possession/marijuana-possession.html$',
        hillsborough_marijuanaposs.marijuanapossession,
        name='hills-marijuana-possession-marijuana-possession'),

    url(r'^fl/hills/marijuana-possession/farr.html$',
        hillsborough_marijuanaposs.farr,
        name='hills-marijuana-possession-farr'),

    url(r'^fl/hills/marijuana-possession/greco.html$',
        hillsborough_marijuanaposs.greco,
        name='hills-marijuana-possession-greco'),

    url(r'^fl/hills/marijuana-possession/jeske.html$',
        hillsborough_marijuanaposs.jeske,
        name='hills-marijuana-possession-jeske'),

    url(r'^fl/hills/marijuana-possession/lefler.html$',
        hillsborough_marijuanaposs.lefler,
        name='hills-marijuana-possession-lefler'),

    url(r'^fl/hills/marijuana-possession/mcneil.html$',
        hillsborough_marijuanaposs.mcneil,
        name='hills-marijuana-possession-mcneil'),

    url(r'^fl/hills/marijuana-possession/myers.html$',
        hillsborough_marijuanaposs.myers,
        name='hills-marijuana-possession-myers'),

    url(r'^fl/hills/marijuana-possession/taylor.html$',
        hillsborough_marijuanaposs.taylor,
        name='hills-marijuana-possession-taylor'),

    url(r'^fl/hills/petit-theft/petittheft.html$',
        hillsborough_petit_theft.petit_theft,
        name='hills-petit-theft-petit-theft'),

    url(r'^fl/hills/petit-theft/farr.html$',
        hillsborough_marijuanaposs.farr,
        name='hills-petit-theft-farr'),

    url(r'^fl/hills/petit-theft/greco.html$',
        hillsborough_marijuanaposs.greco,
        name='hills-petit-theft-greco'),

    url(r'^fl/hills/petit-theft/jeske.html$',
        hillsborough_marijuanaposs.jeske,
        name='hills-petit-theft-jeske'),

    url(r'^fl/hills/petit-theft/lefler.html$',
        hillsborough_marijuanaposs.lefler,
        name='hills-petit-theft-lefler'),

    url(r'^fl/hills/petit-theft/mcneil.html$',
        hillsborough_marijuanaposs.mcneil,
        name='hills-petit-theft-mcneil'),

    url(r'^fl/hills/petit-theft/myers.html$',
        hillsborough_marijuanaposs.myers,
        name='hills-petit-theft-myers'),

    url(r'^fl/hills/petit-theft/taylor.html$',
        hillsborough_marijuanaposs.taylor,
        name='hills-petit-theft-taylor'),


    url(r'^fl/hills/hillsborough-battery.html$',
        hillsborough_battery.hillsborough_battery,
        name='hillsborough-battery'),

    url(r'^fl/hills/hillsborough-marijuanaposs.html$',
        hillsborough_marijuanaposs.hillsborough_marijuanaposs,
        name='hillsborough-marijuanaposs'),

    url(r'^fl/hills/hillsborough-petit-theft.html$',
        hillsborough_petit_theft.hillsborough_petit_theft,
        name='hillsborough-petit-theft'),

    url(r'^fl/hills/hillsborough-dwlsr.html$',
        hillsborough_dwlsr.hillsborough_dwlsr,
        name='hillsborough-dwlsr'),


    url(r'^fl/pinellas/pinellas-dui.html$',
        pinellas_dui.pinellas_dui,
        name='pinellas-dui'),

    url(r'^fl/pinellas/marijuana-possession.html$',
        pinellas_marijuanaposs.pinellas_marijuanaposs,
        name='pinellas-marijuana-possession'),


    url(r'^fl/pinellas/battery.html$',
        pinellas_battery.pinellas_battery,
        name='pinellas-battery'),

    url(r'^fl/pinellas/dwlsr.html$',
        pinellas_dwlsr.pinellas_dwlsr,
        name='pinellas-dwlsr'),

    url(r'^fl/pinellas/petit-theft.html$',
        pinellas_petit_theft.pinellas_petit_theft,
        name='pinellas-petit-theft'),

    url(r'^fl/pinellas/dwlsr/dwlsr.html$',
        pinellas_dwlsr.dwlsr,
        name='pinellas-dwlsr-dwlsr'),

    url(r'^fl/pinellas/dwlsr/bedinghaus.html$',
        pinellas_dwlsr.bedinghaus,
        name='pinellas-dwlsr-bedinghaus'),

    url(r'^fl/pinellas/dwlsr/carballo.html$',
        pinellas_dwlsr.carballo,
        name='pinellas-dwlsr-carballo'),

    url(r'^fl/pinellas/dwlsr/dittmer.html$',
        pinellas_dwlsr.dittmer,
        name='pinellas-dwlsr-dittmer'),

    url(r'^fl/pinellas/dwlsr/horrox.html$',
        pinellas_dwlsr.horrox,
        name='pinellas-dwlsr-horrox'),

    url(r'^fl/pinellas/dwlsr/levine.html$',
        pinellas_dwlsr.levine,
        name='pinellas-dwlsr-levine'),

    url(r'^fl/pinellas/dwlsr/mckyton.html$',
        pinellas_dwlsr.mckyton,
        name='pinellas-dwlsr-mckyton'),

    url(r'^fl/pinellas/dwlsr/overton.html$',
        pinellas_dwlsr.overton,
        name='pinellas-dwlsr-overton'),

    url(r'^fl/pinellas/dwlsr/pierce.html$',
        pinellas_dwlsr.pierce,
        name='pinellas-dwlsr-pierce'),

    url(r'^fl/pinellas/battery/battery.html$',
        pinellas_battery.battery,
        name='pinellas-battery-battery'),

    url(r'^fl/pinellas/battery/bedinghaus.html$',
        pinellas_battery.bedinghaus,
        name='pinellas-battery-bedinghaus'),

    url(r'^fl/pinellas/battery/carballo.html$',
        pinellas_battery.carballo,
        name='pinellas-battery-carballo'),

    url(r'^fl/pinellas/battery/dittmer.html$',
        pinellas_battery.dittmer,
        name='pinellas-battery-dittmer'),

    url(r'^fl/pinellas/battery/horrox.html$',
        pinellas_battery.horrox,
        name='pinellas-battery-horrox'),

    url(r'^fl/pinellas/battery/levine.html$',
        pinellas_battery.levine,
        name='pinellas-battery-levine'),

    url(r'^fl/pinellas/battery/mckyton.html$',
        pinellas_battery.mckyton,
        name='pinellas-battery-mckyton'),

    url(r'^fl/pinellas/battery/overton.html$',
        pinellas_battery.overton,
        name='pinellas-battery-overton'),

    url(r'^fl/pinellas/battery/pierce.html$',
        pinellas_battery.pierce,
        name='pinellas-battery-pierce'),

    url(r'^fl/pinellas/dui/dui.html$',
        pinellas_dui.dui,
        name='pinellas-dui-dui'),

    url(r'^fl/pinellas/dui/bedinghaus.html$',
        pinellas_dui.bedinghaus,
        name='pinellas-dui-bedinghaus'),

    url(r'^fl/pinellas/dui/carballo.html$',
        pinellas_dui.carballo,
        name='pinellas-dui-carballo'),

    url(r'^fl/pinellas/dui/dittmer.html$',
        pinellas_dui.dittmer,
        name='pinellas-dui-dittmer'),

    url(r'^fl/pinellas/dui/horrox.html$',
        pinellas_dui.horrox,
        name='pinellas-dui-horrox'),

    url(r'^fl/pinellas/dui/levine.html$',
        pinellas_dui.levine,
        name='pinellas-dui-levine'),

    url(r'^fl/pinellas/dui/mckyton.html$',
        pinellas_dui.mckyton,
        name='pinellas-dui-mckyton'),

    url(r'^fl/pinellas/dui/overton.html$',
        pinellas_dui.overton,
        name='pinellas-dui-overton'),

    url(r'^fl/pinellas/dui/pierce.html$',
        pinellas_dui.pierce,
        name='pinellas-dui-pierce'),

    url(r'^fl/pinellas/marijuana-possession/marijuana-possession.html$',
        pinellas_marijuanaposs.marijuana_possession,
        name='pinellas-marijuana-possession-marijuana-possession'),

    url(r'^fl/pinellas/marijuana-possession/bedinghaus.html$',
        pinellas_marijuanaposs.bedinghaus,
        name='pinellas-marijuana-possession-bedinghaus'),

    url(r'^fl/pinellas/marijuana-possession/carballo.html$',
        pinellas_marijuanaposs.carballo,
        name='pinellas-marijuana-possession-carballo'),

    url(r'^fl/pinellas/marijuana-possession/dittmer.html$',
        pinellas_marijuanaposs.dittmer,
        name='pinellas-marijuana-possession-dittmer'),

    url(r'^fl/pinellas/marijuana-possession/horrox.html$',
        pinellas_marijuanaposs.horrox,
        name='pinellas-marijuana-possession-horrox'),

    url(r'^fl/pinellas/marijuana-possession/levine.html$',
        pinellas_marijuanaposs.levine,
        name='pinellas-marijuana-possession-levine'),

    url(r'^fl/pinellas/marijuana-possession/mckyton.html$',
        pinellas_marijuanaposs.mckyton,
        name='pinellas-marijuana-possession-mckyton'),

    url(r'^fl/pinellas/marijuana-possession/overton.html$',
        pinellas_marijuanaposs.overton,
        name='pinellas-marijuana-possession-overton'),

    url(r'^fl/pinellas/marijuana-possession/pierce.html$',
        pinellas_marijuanaposs.pierce,
        name='pinellas-marijuana-possession-pierce'),

    url(r'^fl/pinellas/petit-theft/petit-theft.html$',
        pinellas_petit_theft.petit_theft,
        name='pinellas-petit-theft-petit-theft'),

    url(r'^fl/pinellas/petit-theft/bedinghaus.html$',
        pinellas_petit_theft.bedinghaus,
        name='pinellas-petit-theft-bedinghaus'),

    url(r'^fl/pinellas/petit-theft/carballo.html$',
        pinellas_petit_theft.carballo,
        name='pinellas-petit-theft-carballo'),

    url(r'^fl/pinellas/petit-theft/dittmer.html$',
        pinellas_petit_theft.dittmer,
        name='pinellas-petit-theft-dittmer'),

    url(r'^fl/pinellas/petit-theft/horrox.html$',
        pinellas_petit_theft.horrox,
        name='pinellas-petit-theft-horrox'),

    url(r'^fl/pinellas/petit-theft/levine.html$',
        pinellas_petit_theft.levine,
        name='pinellas-petit-theft-levine'),

    url(r'^fl/pinellas/petit-theft/mckyton.html$',
        pinellas_petit_theft.mckyton,
        name='pinellas-petit-theft-mckyton'),

    url(r'^fl/pinellas/petit-theft/overton.html$',
        pinellas_petit_theft.overton,
        name='pinellas-petit-theft-overton'),

    url(r'^fl/pinellas/petit-theft/pierce.html$',
        pinellas_petit_theft.pierce,
        name='pinellas-petit-theft-pierce'),









    #url(r'^pinellas.html$', views.pinellas, name='pinellas'),
]