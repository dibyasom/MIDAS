from django.db import models

from core.models.conference import Conference


class SteeringCommittee(models.Model):
    # Associated conference
    conference = models.OneToOneField(
        Conference,
        on_delete=models.CASCADE,
        related_name="steering_committee",
    )

    # Field maps
    committee_map = models.FileField(default=None, null=True)

    def __str__(self) -> str:
        return "sterring_committee$" + str(self.conference)
