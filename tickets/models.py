from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from ckeditor.fields import RichTextField

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
    description = RichTextField()
    reference_number = models.IntegerField(null=True, blank=True)
    attachment = models.FileField("/downloads", null=True, blank=True)
    reported_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["reported_by", "subject"]
        ordering = ["subject", "reported_by"]

    def __str__(self):
        return f"{self.reported_by} - {self.subject}"


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    author = GenericForeignKey("content_type", "object_id")
    ticket = models.ForeignKey(
        Ticket, on_delete=models.CASCADE, related_name="comments"
    )
    content = RichTextField()
    attachment = models.FileField("/downloads", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at", "ticket"]

    def __str__(self):
        return f"Comment by {self.author} on Ticket {self.ticket.id}"


class ActivityLog(models.Model):
    ACTION_CHOICES = [
        ("status_change", "Status Change"),
        ("assigned", "Assigned"),
        ("commented", "Comment Added"),
        ("reopened", "Reopened"),
    ]

    ticket = models.ForeignKey(
        Ticket, on_delete=models.CASCADE, related_name="activity_logs"
    )
    action_type = models.CharField(max_length=254, choices=ACTION_CHOICES)
    centre = models.ForeignKey(Centre, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_action_type_display()} on Ticket {self.ticket.id} by {self.centre}"
