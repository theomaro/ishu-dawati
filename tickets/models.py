from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Centre(models.Model):
    number = models.CharField(max_length=254, unique=True, primary_key=True)
    name = models.CharField(max_length=254)
    region = models.CharField(max_length=254)
    district = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=245, unique=True)

    class Meta:
        unique_together = ["number", "name"]
        ordering = ["name", "number"]

    def __str__(self):
        return f"{self.number} - {self.name}"


class Ticket(models.Model):
    TYPE_QUESTION = "question"
    TYPE_INCIDENT = "incident"
    TYPE_PROBLEM = "problem"
    TYPE_CHOICES = [
        (TYPE_QUESTION, "Question"),
        (TYPE_INCIDENT, "Incident"),
        (TYPE_PROBLEM, "Problem"),
    ]

    PRIORITY_LOW = "low"
    PRIORITY_MEDIUM = "medium"
    PRIORITY_HIGH = "high"
    PRIORITY_URGENT = "urgent"
    PRIORITY_CHOICES = [
        (PRIORITY_LOW, "Low"),
        (PRIORITY_MEDIUM, "Medium"),
        (PRIORITY_HIGH, "High"),
        (PRIORITY_URGENT, "Urgent"),
    ]

    STATUS_OPEN = "open"
    STATUS_CLOSED = "closed"
    STATUS_ARCHIVE = "archive"
    STATUS_CHOICES = [
        (STATUS_OPEN, "Open or Pending"),
        (STATUS_CLOSED, "Closed or Resolved"),
        (STATUS_ARCHIVE, "Archive"),
    ]

    reported_by = models.ForeignKey(
        Centre, on_delete=models.CASCADE, related_name="created_tickets"
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_tickets",
    )
    subject = models.CharField(max_length=254)
    type = models.CharField(max_length=254, choices=TYPE_CHOICES, default=TYPE_INCIDENT)
    priority = models.CharField(
        max_length=254, choices=PRIORITY_CHOICES, default=PRIORITY_LOW
    )
    status = models.CharField(
        max_length=254, choices=STATUS_CHOICES, default=STATUS_OPEN
    )
    description = models.TextField()
    reference_number = models.IntegerField(null=True, blank=True)
    attachment = models.FileField("/downloads", null=True, blank=True)
    reported_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["reported_by", "subject"]
        ordering = ["subject", "reported_by"]

    def __str__(self):
        return f"{self.reported_by} - {self.subject}"
