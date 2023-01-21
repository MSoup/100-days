from django.contrib.auth import get_user_model
from accountability_app.models import Post
from rest_framework import serializers

User = get_user_model()

# SERIALIZERS
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ["url", "author", "tags", "post_text"]
        lookup_field = "tags"

