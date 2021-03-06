"""techtracking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

import checkout.views

urlpatterns = [
    url(r'^$', checkout.views.index, name='index'),
    url(r'^week/(?P<week_number>[0-9]+)$', checkout.views.week_schedule, name='schedule'),
    url(r'^request/', checkout.views.reserve_request, name='reserve_request'),
    url(r'^reserve/', checkout.views.reserve, name='reserve'),
    url(r'^reservations/', checkout.views.reservations, name='reservations'),
    url(r'^movements/(?P<week_number>[0-9]+)$', checkout.views.week_movements, name='movements'),
    url(r'^movements/', checkout.views.movements, name='movements'),
    url(r'^delete/', checkout.views.delete, name='delete'),
    url(r'^export/', checkout.views.export, name='export'),
    url(r'^change_site/', checkout.views.change_site, name='change_site'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
