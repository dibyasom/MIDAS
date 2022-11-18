from django.db import models

from core.models.conference import Conference


class Speaker(models.Model):
    # For use cases undefined
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # Associated conference
    conference = models.ForeignKey(
        Conference,
        on_delete=models.CASCADE,
        related_name="speakers",
        blank=True, null=True,
    )

    # Org details
    full_name = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    home_location = models.CharField(max_length=100)
    affiliation = models.CharField(max_length=100)
    avatar_image = models.FileField()

    # optional
    website = models.URLField(blank=True)

    def __str__(self) -> str:
        return str(self.full_name)

    class Meta:
        ordering = ["created_at"]
