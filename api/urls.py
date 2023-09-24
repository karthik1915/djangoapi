# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    #
    # html urls
    #
    path(r"imagesapi/", views.images),
    path(r"postsapi/", views.posts),
    path(r"posts/viewposts/", views.ViewPosts),
    #
    # json urls
    #
    path(r"images/", views.ImageList.as_view(), name="image-list"),
    path(r"images/<int:pk>/", views.ImageDetail.as_view(), name="image-detail"),
    path(r"images/random/", views.RandomImageView.as_view(), name="random-image"),
    path(r"posts/", views.PostListCreateView.as_view(), name="post-list-create"),
    path(r"posts/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path(r"posts/vent/", views.VentPostListView.as_view(), name="vent-post-list"),
    path(r"posts/poem/", views.PoemPostListView.as_view(), name="poem-post-list"),
    path(r"posts/convo/", views.ConvoPostListView.as_view(), name="convo-post-list"),
    
    
]
