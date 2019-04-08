from rest_framework import serializers
from .models import Company, Post, Comment, CompanyFavorite, PostFavorite


class CompanyFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyFavorite
        fields = ('company',)

    def create(self, validated_data):
        user = self.context.get('user')
        company = validated_data['company']
        favorite = CompanyFavorite.objects.filter(user=user, company=company)
        if favorite:
            favorite.delete()
        else:
            fav_company = CompanyFavorite.objects.create(user=user, **validated_data)
            fav_company.save()
            return fav_company


class CompanyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('owner', 'name', 'address', 'contacts', 'info', 'logo', 'id',)


class CompanySerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ('owner', 'name', 'address', 'contacts', 'info', 'logo', 'id', 'is_favorite')

    def get_is_favorite(self, obj):
        user = self.context.get('user')
        favorite = CompanyFavorite.objects.filter(user=user, company=obj)
        if favorite:
            return True
        else:
            return False


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'address', 'contacts', 'info', 'logo',)

    def create(self, validated_data):
        owner = self.context.get('owner')
        company = Company.objects.create(owner=owner, **validated_data)
        company.save()
        return company


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'info', 'user_id', 'id')


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'info', 'user_id')


class PostEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'info',)


class PostFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostFavorite
        fields = ('post',)

    def create(self, validated_data):
        user = self.context.get('user')
        fav_post = PostFavorite.objects.create(user=user, **validated_data)
        fav_post.save()
        return fav_post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'post_id', 'id')


class CommentDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'post_id', 'id',)





