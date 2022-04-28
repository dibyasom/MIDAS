from django.db import models

from core.models.conference import Conference


class NationalAdvisoryCommittee(models.Model):
    # Associated conference
    conference = models.OneToOneField(
        Conference, on_delete=models.CASCADE, related_name="national_advisory"
    )


    # Field maps
    committee_map = models.FileField(default=None, null=True)

    def __str__(self) -> str:
        return "national_committee$" + str(self.conference)
