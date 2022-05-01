from django.db import models

from core.models.international_advisory import InternationalAdvisoryCommittee
from core.models.national_advisory import NationalAdvisoryCommittee
from core.models.steering_committee import SteeringCommittee
from core.models.technical_program_committee import TechnicalProgramCommittee


class StakeHolder(models.Model):
    # For use cases undefined
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # Org details
    full_name = models.CharField(max_length=500)
    afiliation = models.CharField(max_length=250, blank=True, null=True)

    # optional
    website = models.URLField(blank=True)

    # ForeignKey
    tp_committee = models.ForeignKey(
        TechnicalProgramCommittee,
        related_name="tpc_members",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    # International
    international_committee = models.ForeignKey(
        InternationalAdvisoryCommittee,
        related_name="international_members",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    # National
    national_committee = models.ForeignKey(
        NationalAdvisoryCommittee,
        related_name="national_members",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    # Steering Comittee
    steering_committee = models.ForeignKey(
        SteeringCommittee,
        related_name="steering_committee",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    # Designation | Stores the roll of a committee member
    designation = models.CharField(max_length=200, blank=True, null=-True)

    def __str__(self) -> str:
        return str(self.full_name)

    class Meta:
        ordering = ["created_at"]
