from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post
from django.contrib.auth import get_user_model
from posts.models import Follow
from posts.models import Group

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')

    def validate_following(self, value):
        request = self.context.get('request')
        if request is None or request.user.is_anonymous:
            return value
        if request.user == value:
            raise serializers.ValidationError('Нельзя подписываться на себя')
        if Follow.objects.filter(user=request.user, following=value).exists():
            raise serializers.ValidationError(
                'Вы уже подписаны на этого пользователя'
            )
        return value


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')
