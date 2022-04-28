from django.db import models

from core.models.conference import Conference


class InternationalAdvisoryCommittee(models.Model):
    # Associated conference
    conference = models.OneToOneField(
        Conference,
        on_delete=models.CASCADE,
        related_name="international_advisory",
    )

    # Field maps
    committee_map = models.FileField(default=None, null=True)

    def __str__(self) -> str:
        return "international_committee$" + str(self.conference)
