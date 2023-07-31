from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.abstract.serializers import AbstractSerializer
from core.user.models import User
from core.user.serializers import UserSerializer
from core.comment.models import Comment
from core.post.models import Post


class CommentSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(
        slug_field="public_id", queryset=User.objects.all()
    )
    post = serializers.SlugRelatedField(
        slug_field="public_id", queryset=Post.objects.all()
    )

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep["author"])
        rep["author"] = UserSerializer(author).data
        return rep

    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You cannot create comment for another user")
        return value

    def validate_post(self, value):
        if self.instance:
            return self.instance.post
        return value

    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data["edited"] = True
        instance = super().update(instance, validated_data)
        return instance

    class Meta:
        model = Comment
        # List all fields to be included in a request and response
        fields = ["id", "post", "author", "body", "edited", "created", "updated"]
        read_only_fields = ["edited"]
