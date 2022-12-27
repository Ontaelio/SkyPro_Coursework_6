from rest_framework import serializers

from ads.models import Comment, Ad


class CommentSerializer(serializers.ModelSerializer):

    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    author_id = serializers.ReadOnlyField(source='author.id')
    author_image = serializers.ReadOnlyField(source='author.image_url')
    ad_id = serializers.ReadOnlyField(source='ad.id')

    class Meta:
        model = Comment
        fields = ('pk', 'text', 'author_id', 'created_at', 'author_first_name', 'author_last_name',
                  'ad_id', 'author_image')


class AdSerializer(serializers.ModelSerializer):
    phone = serializers.ReadOnlyField(source='author.phone')
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    author_id = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Ad
        fields = ('pk', 'image', 'title', 'price', 'description',
                  'phone', 'author_first_name', 'author_last_name', 'author_id')


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text',)
