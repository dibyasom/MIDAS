from django.db import models

from core.models.conference import Conference
from django_better_admin_arrayfield.models.fields import ArrayField


class TrackForPaper(models.Model):
    # For use cases undefined
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # Associated conference
    conference = models.ForeignKey(
        Conference,
        on_delete=models.CASCADE,
        related_name="tracks",
        default=Conference.objects.first().pk,
    )

    # Org details
    title = models.CharField(max_length=75)
    pointers = ArrayField(models.CharField(max_length=250, default=""),null=True, blank=True)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        ordering = ["created_at"]
