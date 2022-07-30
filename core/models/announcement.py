from django.db import models

from core.models.conference import Conference


class Announcement(models.Model):
    # For use cases undefined
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # Associated conference
    conference = models.ForeignKey(
        Conference,
        on_delete=models.CASCADE,
        related_name="announcements",
        default=Conference.objects.first().pk,
    )

    # Content for announcement
    title = models.CharField(max_length=75)
    url = models.URLField(blank=True)
    description = models.TextField(max_length=250, blank=True)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        ordering = ["created_at"]
