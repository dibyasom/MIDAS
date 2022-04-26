from django.shortcuts import render

# from core.models.announcement import Announcement

from core.models.conference import Conference

# from core.models.technical_partner import TechnicalPartner

# Create your views here.
def render_landing_page(request, uniquename):
    pass


def render_latest_conference(request):
    # Render the most recently created

    # Fetch the most-recently scheduled event
    Conference.objects.order_by("-created_at")
    conference: Conference = Conference.objects.first()

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
            "speakers": conference.speakers.all()
        },
    )
