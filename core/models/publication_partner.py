from django.db import models

from core.models.conference import Conference


class PublicationPartner(models.Model):
    # For use cases undefined
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # Associated conference
    conference = models.ForeignKey(
        Conference,
        on_delete=models.CASCADE,
        related_name="publication_partners",
        default=Conference.objects.first(),
    )

    # Org details
    org_name = models.CharField(max_length=50)
    website = models.URLField(blank=True)
    logo = models.FileField()

    def __str__(self) -> str:
        return str(self.org_name)

    class Meta:
        ordering = ["created_at"]
