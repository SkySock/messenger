from django.db import models
from django.conf import settings


class UserFollowing(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following'
    )
    following_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followers'
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'following_user'],  name='unique_followers',)
        ]

        ordering = ['-created']

    def __str__(self):
        return f"{self.user} follows {self.following_user}"
