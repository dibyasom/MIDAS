from django.db import models

from core.models.conference import Conference
from core.models.stakeholder import StakeHolder


class OrganisingCommittee(models.Model):
    # Associated conference
    conference = models.OneToOneField(
        Conference,
        on_delete=models.CASCADE,
    )

    # One to one fields
    organising_chair = models.OneToOneField(
        StakeHolder, on_delete=models.CASCADE, related_name="organising_chair"
    )

    # Many to many fields
    organising_co_chair = models.ManyToManyField(StakeHolder, related_name="co_chairs")

    organising_committee = models.ManyToManyField(
        StakeHolder, related_name="committees"
    )
    publicity_and_sponsorship_chair = models.ManyToManyField(
        StakeHolder, related_name="publicity_and_sponsor_chairs"
    )
    web_chair = models.ManyToManyField(StakeHolder, related_name="web_chairs")

    def __str__(self) -> str:
        return "organising_committee$" + str(self.conference)
