from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Follow,  Post, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['username']
        model = User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Post


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    def validate_following(self, following):

        user = self.context['request'].user

        if user != following:

            return following

        raise serializers.ValidationError('cant subscribe')

    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            ),
        ]


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Post
