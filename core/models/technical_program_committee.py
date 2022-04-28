from django.db import models

from core.models.conference import Conference


class TechnicalProgramCommittee(models.Model):
    # Associated conference
    conference = models.OneToOneField(
        Conference,
        on_delete=models.CASCADE,
        related_name="technical_program",
    )

    # Field maps
    committee_map = models.FileField(default=None, null=True)

    def __str__(self) -> str:
        return "technical_program_committee$" + str(self.conference)
