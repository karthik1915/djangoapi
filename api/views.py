import random
import requests
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Image, Post
from .serializers import ImageSerializer, PostSerializer


def index(request):
    context = {"title": "HOME", "content": "This is the home page"}
    return render(request, "apihome.html", context)


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def images(request):
    api_url = (
        "http://127.0.0.1:8000/api/images/random"  # Use the name of your URL pattern
    )
    response = requests.get(api_url)

    if response.status_code == 200:
        api_data = response.json()  # Parse the JSON response
        context = {"title":"Images" , "api_response": api_data, "status_code": response.status_code}
        return render(request, "img_api.html", context)
    else:
        context = {
            "api_response": "Error occurred while getting data",
            "status_code": response.status_code,
        }
        return render(request, "img_api.html", context)


def posts(request):
    context = {"title": "Posts", "content": "This is the home page"}
    return render(request, "post_api.html", context)

def ViewPosts(request):
    api_url = (
        "http://127.0.0.1:8000/api/posts"  # Use the name of your URL pattern
    )

    response = requests.get(api_url)
    if response.status_code == 200:
        api_data = response.json()  # Parse the JSON response
        
        context = {"api_response": api_data, "status_code": response.status_code}
        return render(request, "postsView.html", context)
    else:
        context = {
            "api_response": "Error occurred while getting data",
            "status_code": response.status_code,
        }
        return render(request, "postsView.html", context)


class ImageList(generics.ListAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        queryset = Image.objects.all()

        # Get the 'category' query parameter from the URL
        category = self.request.query_params.get("category")

        # Filter the queryset based on the 'category' parameter
        if category:
            queryset = queryset.filter(category=category)

        return queryset


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class RandomImageView(generics.ListAPIView):
    def get(self, request):
        random_image = random.choice(Image.objects.all())
        serializer = ImageSerializer(random_image)
        return Response(serializer.data)


class PostListCreateView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class VentPostListView(generics.ListAPIView):
    queryset = Post.objects.filter(type="vent")
    serializer_class = PostSerializer


class PoemPostListView(generics.ListAPIView):
    queryset = Post.objects.filter(type="poem")
    serializer_class = PostSerializer


class ConvoPostListView(generics.ListAPIView):
    queryset = Post.objects.filter(type="convo")
    serializer_class = PostSerializer
