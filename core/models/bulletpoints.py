from django.db import models

from core.models.conference import Conference


class BulletPoint(models.Model):
    # For use cases undefined
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # Associated conference
    conference = models.ForeignKey(
        Conference,
        on_delete=models.CASCADE,
        related_name="bulletpoints",
        default=Conference.objects.first().pk,
    )

    # Org details
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    avatar_image = models.FileField()

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        ordering = ["created_at"]
