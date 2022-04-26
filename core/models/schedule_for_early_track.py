from django.db import models
from core.models.conference import Conference

class ScheduleForEarlyTrack(models.Model):
    # For use cases undefined
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # Associated conference
    conference = models.OneToOneField(
        Conference,
        on_delete=models.CASCADE,
        related_name="early_track_schedule",
    )

    # Org details
    last_date = models.DateField()
    author_notification = models.DateField()
    registration_deadline = models.DateField()
    conference_dates = models.DateField()

    def __str__(self) -> str:
        return str(self.conference)

    class Meta:
        ordering = ["created_at"]
