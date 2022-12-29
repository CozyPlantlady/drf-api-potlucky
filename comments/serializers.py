from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        if value-size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size too large. Keep it under 2MB'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width over 4096px, choose a smaller picture'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height over 4096px, choose a smaller picture'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'created_at', 'edited_at',
            'original_recipe', 'image', 'content', 'profile_image',
            'profile_id',
        ]


class CommentDetailSerializer(CommentSerializer):
    post = serializers.ReadOnlyField(source='recipe.id')
