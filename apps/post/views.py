from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


def render_index(request):
    context = {
        'posts':Post.objects.order_by("-id")
    }

    return render(request, 'pages/index.html', context)


def render_edit_blog_post(request, post_id=None):
    post = Post.objects.get(id=post_id) if post_id else None

    serializer = PostSerializer(post)

    context = {
        'post_serializer':serializer,
        'method':'put' if post else 'post',
    }

    return render(request, 'pages/create_edit_post.html', context)



def render_blog_post(request, post_id):
    post = get_object_or_404(Post.objects.all(), id=post_id)
    context = {
        'post':post
    }
    return render(request, 'pages/view_post.html', context)



class BlogPostViewSet(APIView):

    def post(self, request, _):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)







