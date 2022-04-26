from django.db import models

from core.models.conference import Conference
from core.models.stakeholder import StakeHolder


class SteeringCommittee(models.Model):
    # Associated conference
    conference = models.OneToOneField(
        Conference,
        on_delete=models.CASCADE,
    )
    # One to one fields
    chief_patron = models.OneToOneField(
        StakeHolder, on_delete=models.CASCADE, related_name="chief_patron"
    )
    patron = models.OneToOneField(
        StakeHolder, on_delete=models.CASCADE, related_name="patron"
    )
    convener = models.ManyToManyField(StakeHolder, related_name="convener")

    # Many to many fields
    co_patron = models.ManyToManyField(StakeHolder, related_name="co_patrons")

    general_chair = models.ManyToManyField(StakeHolder, related_name="general_chairs")
    general_co_chair = models.ManyToManyField(
        StakeHolder, related_name="general_co_chairs"
    )
    honorary_chair = models.ManyToManyField(StakeHolder, related_name="honorary_chairs")
    advisory_chair = models.ManyToManyField(StakeHolder, related_name="advisory_chairs")
    conference_chair = models.ManyToManyField(
        StakeHolder, related_name="conference_chairs"
    )
    tpc_chair = models.ManyToManyField(StakeHolder, related_name="tpc_chairs")
    tpc_co_chair = models.ManyToManyField(StakeHolder, related_name="tpc_co_chairs")
    track_chair = models.ManyToManyField(StakeHolder, related_name="track_chairs")
    publicity_chair = models.ManyToManyField(
        StakeHolder, related_name="publicity_chairs"
    )
    editorial_board = models.ManyToManyField(
        StakeHolder, related_name="editorial_boards"
    )
    special_session_chair = models.ManyToManyField(
        StakeHolder, related_name="special_session_chairs"
    )
    corporate_chair = models.ManyToManyField(
        StakeHolder, related_name="corporate_chairs"
    )
    co_convener = models.ManyToManyField(StakeHolder, related_name="co_conveners")

    def __str__(self) -> str:
        return "sterring_committee$" + str(self.conference)
