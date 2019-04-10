from django.urls import path
from .views import CompanyListView, CompanyDetailView, CompanyCreate, CompanyEditView, \
    CompanyDeleteView, PostListView, PostCreateView, PostDetailView, PostEditView, \
    PostDeleteView, CommentListView, CommentCreateView, CommentEditView, CompanyFavoriteView, MyCompanyListView, \
    CommentDeleteView, MyFavoriteListView, CommentDetailView, MyPostListView


urlpatterns = [
    path('', CompanyListView.as_view()),
    path('<int:pk>/', CompanyDetailView.as_view()),
    path('create/', CompanyCreate.as_view()),
    path('edit/<int:pk>/', CompanyEditView.as_view()),
    path('delete/<int:pk>/', CompanyDeleteView.as_view()),
    path('favorite/create/', CompanyFavoriteView.as_view()),
    path('favorite/', MyFavoriteListView.as_view()),
    path('my_list/', MyCompanyListView.as_view()),

    path('post/', PostListView.as_view()),
    path('post/create/', PostCreateView.as_view()),
    path('post/<int:pk>/', PostDetailView.as_view(),),
    path('post/edit/<int:pk>/', PostEditView.as_view()),
    path('post/delete/<int:pk>/', PostDeleteView.as_view()),
    path('my_posts/', MyPostListView.as_view()),

    path('comment/', CommentListView.as_view()),
    path('comment/create/', CommentCreateView.as_view()),
    path('comment/edit/<int:pk>/', CommentEditView.as_view()),
    path('comment/delete/<int:pk>/', CommentDeleteView.as_view()),
    path('comment/<int:pk>/', CommentDetailView.as_view())
]
