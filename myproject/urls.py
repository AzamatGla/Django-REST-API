from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from .views import signup

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('signup/', signup, name='signup'),
    path('company/', include('myapp.urls')),
]
