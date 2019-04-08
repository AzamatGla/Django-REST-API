from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.pagination import LimitOffsetPagination
from .serializers import CompanySerializer, CompanyCreateSerializer, PostSerializer, PostCreateSerializer, \
    CommentSerializer, CompanyFavoriteSerializer, CompanyListSerializer, PostFavoriteSerializer
from .models import Company, Post, Comment, CompanyFavorite
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .permissions import IsCompanyOwner, IsCompanyPostOwner, IsCompanyCommentOwner
from rest_framework.response import Response


class CompanyFavoriteView(generics.CreateAPIView):
    serializer_class = CompanyFavoriteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        context = super(CompanyFavoriteView, self).get_serializer_context()
        context.update({
            "user": self.request.user
        })
        return context

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        company = Company.objects.get(pk=request.data['company'])
        user = self.request.user
        favorite = CompanyFavorite.objects.filter(user=user, company=company)
        if favorite:
            favorite.delete()
            return Response({'Компания удалена из Избранных '},
                            status=status.HTTP_204_NO_CONTENT)
        else:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({'Компания успешно добавлена в Избранное'}, status=status.HTTP_201_CREATED, headers=headers)


class CompanyListPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 1000


class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer
    pagination_class = CompanyListPagination
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filterset_fields = ('name', 'address', 'contacts', 'info', 'owner')
    search_fields = ('name', 'address', 'contacts', 'info')


class MyCompanyListView(generics.ListAPIView):
    serializer_class = CompanyListSerializer

    def get_queryset(self):
        return Company.objects.filter(owner=self.request.user)


class CompanyCreate(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyCreateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_serializer_context(self):
        context = super(CompanyCreate, self).get_serializer_context()
        context.update({
            "owner": self.request.user
        })
        return context


class CompanyDetailView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_serializer_context(self):
        context = super(CompanyDetailView, self).get_serializer_context()
        context.update({
            "user": self.request.user
        })
        return context


class CompanyEditView(generics.UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer
    permission_classes = (IsAuthenticated, IsCompanyOwner,)
    authentication_classes = (TokenAuthentication,)


class CompanyDeleteView(generics.DestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer
    permission_classes = (IsAuthenticated, IsCompanyOwner,)
    authentication_classes = (TokenAuthentication,)


class PostFavoriteView(generics.CreateAPIView):
    serializer_class = PostFavoriteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        context = super(PostFavoriteView, self).get_serializer_context()
        context.update({
            "user": self.request.user
        })
        return context


class PostListPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 1000


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostListPagination
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filterset_fields = ('title', 'info', 'user_id', 'id',)
    search_fields = ('title', 'info',)


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        company = Company.objects.get(pk=request.data['user_id'])
        if company.owner == self.request.user:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({'Объявление успешно создано'}, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'Вы не можете создать объявление от имени компании, которая вам не принадлежит'},
                            status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostEditView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsCompanyPostOwner)
    authentication_classes = (TokenAuthentication,)


class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsCompanyPostOwner)
    authentication_classes = (TokenAuthentication,)


class CommentListPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 50


class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CommentListPagination
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filterset_fields = ('text', 'post_id')
    search_fields = ('text', 'post_id',)


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class CommentEditView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsCompanyCommentOwner,)
    authentication_classes = (TokenAuthentication,)


class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsCompanyCommentOwner,)
    authentication_classes = (TokenAuthentication,)
