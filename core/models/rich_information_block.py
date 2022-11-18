from django.db import models
from core.models.conference import Conference


class RichInformationBlock(models.Model):
    # For use cases undefined
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # Associated conference
    conference = models.ForeignKey(
        Conference,
        on_delete=models.CASCADE,
        related_name="rich_information_block",
        blank=True, null=True,
    )

    # Org details
    content = models.TextField()
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        ordering = ["created_at"]
