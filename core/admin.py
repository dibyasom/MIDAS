from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from core.models import (
    conference,
    schedule_for_early_track,
    schedule_for_regular_track,
    stakeholder,
    venue,
    announcement,
    track_for_paper,
    technical_partner,
    publication_partner,
    bulletpoints,
    national_advisory,
    international_advisory,
    organising_committee,
    student_organising_committee,
    special_session,
    technical_program_committee,
    speaker,
    stakeholder,
    steering_committee,
)


@admin.register(
    conference.Conference,
    venue.Venue,
    announcement.Announcement,
    schedule_for_early_track.ScheduleForEarlyTrack,
    schedule_for_regular_track.ScheduleForRegularTrack,
    technical_partner.TechnicalPartner,
    publication_partner.PublicationPartner,
    bulletpoints.BulletPoint,
    speaker.Speaker,
    stakeholder.StakeHolder,
    steering_committee.SteeringCommittee,
    national_advisory.NationalAdvisoryCommittee,
    international_advisory.InternationalAdvisoryCommittee,
    organising_committee.OrganisingCommittee,
    student_organising_committee.StudentOrganisingCommittee,
    special_session.SpecialSession,
    technical_program_committee.TechnicalProgramCommittee,
)
class UniversalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]


@admin.register(track_for_paper.TrackForPaper)
class TrackForPaperAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ("conference", "title", "pointers")
