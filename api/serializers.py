from rest_framework.serializers import ModelSerializer
from .models import Post, User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.first_name
        token['username'] = user.username
        # ...

        return token


class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class PostSerializers(ModelSerializer):
    # author = UserSerializers(read_only=True)
    class Meta:
        model = Post
        fields = ('id','author', 'title', 'description','created_at', 'updated_at')
