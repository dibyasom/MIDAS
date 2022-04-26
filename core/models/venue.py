from django.db import models

from core.models.conference import Conference


class Venue(models.Model):
    # For use cases undefined
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # Associated conference
    conference = models.OneToOneField(
        Conference,
        on_delete=models.CASCADE,
        related_name="venue",
    )

    # Organizing University
    university = models.CharField(max_length=100)

    # University location
    home_city = models.CharField(max_length=50, blank=True)
    home_state = models.CharField(max_length=50, blank=True)
    home_country = models.CharField(max_length=50)

    # Date
    start_date = models.DateField()
    end_date = models.DateField()

    # University website
    website_url = models.URLField(default="/")

    # Cover image
    cover_image = models.FileField()

    # Organizing domain from university
    university_logo = models.FileField()

    # About
    university_description = models.TextField(max_length=350)

    def __str__(self) -> str:
        return str(self.university) + "@" + str(self.start_date)

    class Meta:
        ordering = ["created_at"]
