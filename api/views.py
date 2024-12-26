from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import PostSerializers
from .models import Post
# from rest_framework.views import APIView, Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

# class PostAPIView(APIView):
#     def get(self, value):
#         posts = Post.objects.all()
#         serializers = PostSerializers(posts, many=True)
#         return Response(serializers.data)

# class PostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers


# class PostCreateAPIView(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class PostListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['title', 'author']
    search_fields = ['author__username', 'title']
    ordering_fields = ['created_at', 'username']
#
# class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthorOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers



                                    # ViewSet
class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly, IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['title', 'author']
    search_fields = ['author__username', 'title']
    ordering_fields = ['created_at', 'username']