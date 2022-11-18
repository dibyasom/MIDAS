from django.db import models

from core.models.conference import Conference


class Fee(models.Model):
    # For use cases undefined
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # Associated conference
    conference = models.ForeignKey(
        Conference,
        on_delete=models.CASCADE,
        related_name="fees",
        blank=True, null=True,
    )

    name_for_category = models.CharField(
        max_length=75, verbose_name="Fee type (As in regular, early ...)"
    )

    def __str__(self) -> str:
        return str(self.name_for_category)

    class Meta:
        ordering = ["created_at"]
