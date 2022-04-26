from django.db import models


class Conference(models.Model):
    # For use cases undefined
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # Organizing University
    title = models.CharField(
        max_length=100,
        default="INTERNATIONAL CONFERENCE ON MACHINE INTELLIGENCE & DATA SCIENCE APPLICATIONS - MIDAS",
    )

    # Description
    about = models.TextField(max_length=5000)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        ordering = ["created_at"]
