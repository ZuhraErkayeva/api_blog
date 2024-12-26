from django.db import router
from django.urls import path
from .views import PostViewSet,PostListAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'api'
urlpatterns = [
    path('list/', PostListAPIView.as_view()),
    # path('detail/<int:pk>/', PostDetailAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("", PostViewSet, basename='post')
urlpatterns += router.urls
