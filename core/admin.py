from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

# Import pandas for excel processing
import pandas as pd

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
    fee,
    fee_type,
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
    organising_committee.OrganisingCommittee,
    student_organising_committee.StudentOrganisingCommittee,
    special_session.SpecialSession,
    fee.Fee,
    fee_type.FeeType,
)
class UniversalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]


@admin.register(track_for_paper.TrackForPaper)
class TrackForPaperAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ("conference", "title", "pointers")


# Models with custom save behaviour - Allows instance creation from excel entries
@admin.register(
    national_advisory.NationalAdvisoryCommittee,
)
class NationalAdvisoryAdmin(admin.ModelAdmin):
    def save_model(
        self, request, obj: national_advisory.NationalAdvisoryCommittee, form, change
    ) -> None:

        # Read excel file
        committee_map = pd.read_excel(obj.committee_map)

        # Save and create ind
        obj.save()

        # Iterate through entries
        for index, row in committee_map.iterrows():
            salutation, full_name, designation, affiliation = (
                row["Salutation"],
                row["Full Name"],
                row["Designation"],
                row["Affiliation"],
            )

            # Append FOreignKey fields
            stakeholder.StakeHolder.objects.create(
                national_committee=obj,
                full_name=f"{salutation}{full_name}",
                afiliation=affiliation,
            )

        return super().save_model(request, obj, form, change)


@admin.register(
    international_advisory.InternationalAdvisoryCommittee,
)
class InternationalAdvisoryAdmin(admin.ModelAdmin):
    def save_model(
        self, request, obj: national_advisory.NationalAdvisoryCommittee, form, change
    ) -> None:

        # Read excel file
        committee_map = pd.read_excel(obj.committee_map)

        # Save and create ind
        obj.save()

        # Iterate through entries
        for index, row in committee_map.iterrows():
            salutation, full_name, designation, affiliation = (
                row["Salutation"],
                row["Full Name"],
                row["Designation"],
                row["Affiliation"],
            )

            # Append FOreignKey fields
            stakeholder.StakeHolder.objects.create(
                international_committee=obj,
                full_name=f"{salutation}{full_name}",
                afiliation=affiliation,
            )

        return super().save_model(request, obj, form, change)


@admin.register(
    technical_program_committee.TechnicalProgramCommittee,
)
class TpcAdmin(admin.ModelAdmin):
    def save_model(
        self, request, obj: national_advisory.NationalAdvisoryCommittee, form, change
    ) -> None:

        # Read excel file
        committee_map = pd.read_excel(obj.committee_map)

        # Save and create ind
        obj.save()

        # Iterate through entries
        for index, row in committee_map.iterrows():
            salutation, full_name, designation, affiliation = (
                row["Salutation"],
                row["Full Name"],
                row["Designation"],
                row["Affiliation"],
            )

            # Append FOreignKey fields
            stakeholder.StakeHolder.objects.create(
                tp_committee=obj,
                full_name=f"{salutation}{full_name}",
                afiliation=affiliation,
            )

        return super().save_model(request, obj, form, change)


@admin.register(
    steering_committee.SteeringCommittee,
)
class TpcAdmin(admin.ModelAdmin):
    def save_model(
        self, request, obj: steering_committee.SteeringCommittee, form, change
    ) -> None:

        # Read excel file
        committee_map = pd.read_excel(obj.committee_map)

        # Save and create ind
        obj.save()

        # Iterate through entries
        for index, row in committee_map.iterrows():
            full_name, designation, = (
                row["Full Name"],
                row["Designation"],
            )

            # Append FOreignKey fields
            stakeholder.StakeHolder.objects.create(
                steering_committee=obj,
                full_name=f"{full_name}",
                designation=designation,
            )

        return super().save_model(request, obj, form, change)
