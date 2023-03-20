from django.db import models

class Functionnality(models.Model):

    name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    description = models.TextField(
        max_length=500,
        null=False,
        blank=False
    )

    def __str__(self) -> str:
        return f"{self.name} - {self.description}"
    
    class Meta:
        verbose_name_plural = "functionnalities"