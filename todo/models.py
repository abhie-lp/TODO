from django.db import models
from django.utils import timezone
from django.shortcuts import reverse


class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    PRIORITY = (
        (1, "High"),
        (2, "Medium"),
        (3, "Low"),
    )
    priority = models.PositiveSmallIntegerField(choices=PRIORITY, default=3)
    date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = "date", "priority",
        
    def get_absolute_url(self):
        return reverse("todo_list")
