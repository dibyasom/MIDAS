from django.db import models

from core.models.conference import Conference
from core.models.stakeholder import StakeHolder


class NationalAdvisoryCommittee(models.Model):
    # Associated conference
    conference = models.OneToOneField(
        Conference,
        on_delete=models.CASCADE,
    )

    # Many to many fields
    committee = models.ManyToManyField(
        StakeHolder, related_name="national_advisories"
    )

    def __str__(self) -> str:
        return "organising_committee$" + str(self.conference)
