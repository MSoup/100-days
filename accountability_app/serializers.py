from django.contrib.auth import get_user_model
from accountability_app.models import Post, Tag
from rest_framework import serializers

User = get_user_model()

# SERIALIZERS
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    text = serializers.ReadOnlyField(source="post_text")
    date = serializers.DateTimeField(source="pub_date", format="%Y-%m-%d %H:%M:%S")
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "text",
            "date",
            "tags",
        ]


class TagSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField()

    class Meta:
        model = Tag
        fields = ["name"]
