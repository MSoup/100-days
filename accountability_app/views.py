from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth import get_user_model

from rest_framework import viewsets

from accountability_app.models import Post
from accountability_app.serializers import UserSerializer, PostSerializer

User = get_user_model()

# VIEWSETS
# ViewSets define the view behavior
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer




def index(request):
    latest_posts_list = Post.objects.order_by("-pub_date")[:15]
    context = {
        "latest_posts_list": latest_posts_list,
    }
    return render(request, "accountability_app/index.html", context)


def detail(request, post_id):
    # post contains author, pub_date, post_text
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "accountability_app/detail.html", {"post": post})


def new_post(request):
    if request.method == "GET":
        return HttpResponse("This endpoint is reserved for post requests")

    if request.method == "POST":
        # if request.user.is_authenticated:
        User = get_user_model()
        # get first user for now
        author = User.objects.get(id=1)
        post_text = request.POST["new_post"]
        new_post = Post(post_text=post_text, pub_date=timezone.now(), author=author)
        new_post.save()
        print("Saved new post:", new_post.post_text)
        # else:

    return HttpResponse("Success")
