from newssite.models import Post
from newssite.models import Category
from taggit.models import Tag
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')



class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')


class PostSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField('one_row')
    category1 = CategorySerializer(source='first_category')
    tags = TagSerializer(many=True)

    def one_row(self, obj):
        c = obj.category.first()
        serializer = CategorySerializer(instance=c)
        return serializer.data

    class Meta:
        model = Post
        fields = ('id', 'title', 'code', 'summary', 'language', 'slug', 'category', 'count_view',
                  'publish_time', 'tags', 'category1')
