from django.db import models

from core.models.conference import Conference


class SpecialSession(models.Model):
    # For use cases undefined
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # Associated conference
    conference = models.ForeignKey(
        Conference,
        on_delete=models.CASCADE,
        related_name="special_sessions",
        default=Conference.objects.first().pk,
    )

    # Org details
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    RSVP_url = models.URLField(blank=True, null=True)
    scheduled_for = models.CharField(max_length=100)
    session_chairs = models.TextField(max_length=100)

    # optional
    website = models.URLField(blank=True)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        ordering = ["created_at"]
