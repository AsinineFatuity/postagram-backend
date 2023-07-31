from django.db import models
from core.abstract.models import AbstractModel, AbstractManager


class PostManager(AbstractManager):
    pass


class Post(AbstractModel):
    author = models.ForeignKey(to="core_user.User", on_delete=models.CASCADE)
    body = models.TextField()
    edited = models.BooleanField(default=False)
    objects = PostManager()

    class Meta:
        db_table = "'core.post'"

    def __str__(self) -> str:
        return f"{self.author.name}"