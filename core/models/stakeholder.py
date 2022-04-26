from django.db import models


class StakeHolder(models.Model):
    # For use cases undefined
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # Org details
    full_name = models.CharField(max_length=100)
    afiliation = models.CharField(max_length=250)

    # optional
    website = models.URLField(blank=True)

    def __str__(self) -> str:
        return str(self.full_name)

    class Meta:
        ordering = ["created_at"]
