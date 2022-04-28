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

    # Associated easy-chair portal
    easy_chair_submission_url = models.URLField(default="#", blank="True")

    # Unique name
    unique_address = models.CharField(
        unique=True,
        max_length=20,
        default="dibylab",
        help_text="A unique name which can be mapped to the event and used in url {https://<domain>/uniquename}. Eg> midas2022",
    )

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        ordering = ["created_at"]
