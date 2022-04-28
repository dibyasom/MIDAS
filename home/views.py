from django.shortcuts import render

# from core.models.announcement import Announcement

from core.models.conference import Conference
from core.models.stakeholder import StakeHolder

# from core.models.technical_partner import TechnicalPartner

# Create your views here.
def render_landing_page(request, uniquename):
    return render(request, "landing_page.html")


def render_tpc(request, uniquename):
    # Fetch conference
    try:
        conference = Conference.objects.get(unique_address=uniquename)
        return render(
            request,
            "committee_template.html",
            {
                "conference": conference,
                "committee_title": "Technical Program Committee",
                "committee": conference.technical_program.tpc_members.all(),
            },
        )
    except Exception as err:
        print("ERROR - TPC", err)
        return render(request, "404.html")


def render_national_committee(request, uniquename):
    # Fetch conference
    try:
        conference = Conference.objects.get(unique_address=uniquename)
        return render(
            request,
            "committee_template.html",
            {
                "conference": conference,
                "committee": conference.national_advisory.national_members.all(),
                "committee_title": "National Advisory Committee",
            },
        )
    except Exception as err:
        print("ERROR - NATIONAL ADVISORY", err)
        return render(request, "404.html")


def render_international_committee(request, uniquename):
    # Fetch conference
    try:
        conference = Conference.objects.get(unique_address=uniquename)
        return render(
            request,
            "committee_template.html",
            {
                "conference": conference,
                "committee": conference.international_advisory.international_members.all(),
                "committee_title": "International Advisory Committee",
            },
        )
    except Exception as err:
        print("ERROR - NATIONAL ADVISORY", err)
        return render(request, "404.html")


def render_tracks(request, uniquename):
    # Fetch conference
    try:
        conference = Conference.objects.get(unique_address=uniquename)
        return render(
            request,
            "tracks.html",
            {
                "conference": conference,
                "tracks": conference.tracks.all(),
            },
        )
    except:
        return render(request, "404.html")


def render_latest_conference(request):
    # Render the most recently created

    # Fetch the most-recently scheduled event
    Conference.objects.order_by("-created_at")
    conference: Conference = Conference.objects.first()

    # Render confernce template w details
    try:
        return render(
            request,
            "landing_page.html",
            {
                "conference": conference,
                "announcements": conference.announcements.all(),
                "no_of_announcements": len(conference.announcements.all()),
                "technical_partners": conference.technical_partners.all(),
                "publication_partners": conference.publication_partners.all(),
                "early_schedule": conference.early_track_schedule,
                "regular_schedule": conference.early_regular_schedule,
                "speakers": conference.speakers.all(),
            },
        )
    except Exception as err:
        print("ERROR- LANDING PAGE: ", err)
        return render(request, "404.html")
