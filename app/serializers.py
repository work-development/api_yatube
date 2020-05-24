from rest_framework import serializers
from posts.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)
    class Meta:
        fields = ('text', 'image',  'pub_date', 'author', 'id')
        model = Post

        

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)
    # author = serializers.CharField( source="author.username", read_only=True)
    class Meta:
        fields = ('text', 'post', 'created', 'author', 'id')
        model = Comment
    def get_author(self, obj):
        return obj.author.username