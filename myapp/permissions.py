from rest_framework.permissions import BasePermission
from .models import Company, Post, Comment


class IsCompanyOwner(BasePermission):
    def has_permission(self, request, view):
        if 'pk' not in view.kwargs:
            return False
        company = Company.objects.get(pk=view.kwargs['pk'])
        if company.owner == request.user:
            return True


class IsCompanyPostOwner(BasePermission):
    def has_permission(self, request, view):
        if 'pk'not in view.kwargs:
            return False
        post = Post.objects.get(pk=view.kwargs['pk'])
        if post.user_id.owner == request.user:
            return True


class IsCompanyCommentOwner(BasePermission):
    def has_permission(self, request, view):
        if 'pk' not in view.kwargs:
            return False
        comment = Comment.objects.get(pk=view.kwargs['pk'])
        if comment.post_id.user_id == request.user:
            return True


