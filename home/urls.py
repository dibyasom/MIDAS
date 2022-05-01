"""midas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from home import views

urlpatterns = [
    # path("<str:uniquename>", views.render_landing_page),
    path("", views.render_latest_conference),
    # Render track details
    path("tracks/<str:uniquename>", views.render_tracks),
    path("technicalprogramcommittee/<str:uniquename>", views.render_tpc),
    path("nationaladvisory/<str:uniquename>", views.render_national_committee),
    path(
        "internationaladvisory/<str:uniquename>", views.render_international_committee
    ),
    path("steeringcommittee/<str:uniquename>", views.render_steering_committee),
]
