from django.shortcuts import render

# from core.models.announcement import Announcement

from core.models.conference import Conference
from core.models.stakeholder import StakeHolder

# from core.models.technical_partner import TechnicalPartner

# Create your views here.
def render_landing_page(request, uniquename):
    try:
        # Get conference
        conference = Conference.objects.get(unique_address=uniquename)
        # Render confernce template w details
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


def render_steering_committee(request, uniquename):
    try:
        # Get associate conference
        conference = Conference.objects.get(unique_address=uniquename)

        # For steering_committee, create dict -> key:disgnation, value:fullname+affiliation
        steering_committee_members = (
            conference.steering_committee.steering_committee.all()
        )

        steering_committee_dict = dict()

        for member in steering_committee_members:
            try:
                _ = steering_committee_dict[member.designation]
                steering_committee_dict[member.designation].append(member.full_name)
            except:
                # Key not present - create a list <3
                steering_committee_dict[member.designation] = [
                    member.full_name,
                ]

        steering_committee_designations = list()
        steering_committee_members_collection = list()

        for _designation, _members in steering_committee_dict.items():
            steering_committee_designations.append(_designation)
            steering_committee_members_collection.append(_members)

        return render(
            request,
            "committee_template_4_steering.html",
            {
                "conference": conference,
                "steering_committee_designations": steering_committee_designations,
                "steering_committee_members_collection": steering_committee_members_collection,
                "steering_committee_dict": steering_committee_dict,
                "committee_title": "Steering Committee",
                "no_affiliation": True,
            },
        )
    except Exception as err:
        print("ERROR - STEERING COMMITTEE", err)
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
                "bulletpoints": conference.bulletpoints.all(),
            },
        )
    except Exception as err:
        print("ERROR- LANDING PAGE: ", err)
        return render(request, "404.html")
