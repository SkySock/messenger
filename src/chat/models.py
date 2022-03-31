from django.db import models
from django.conf import settings


class Room(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="rooms")
    current_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="current_rooms", blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Room(Name: {self.name}, Owner: {self.owner})"


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="messages")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="messages")
    text = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message(User: {self.user}, Room: {self.room})"


class Content(models.Model):
    pass
