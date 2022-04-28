from django.db import models

from core.models.international_advisory import InternationalAdvisoryCommittee
from core.models.national_advisory import NationalAdvisoryCommittee
from core.models.technical_program_committee import TechnicalProgramCommittee


class StakeHolder(models.Model):
    # For use cases undefined
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # Org details
    full_name = models.CharField(max_length=100)
    afiliation = models.CharField(max_length=250)

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

    def __str__(self) -> str:
        return str(self.full_name)

    class Meta:
        ordering = ["created_at"]
