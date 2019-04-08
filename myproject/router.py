from myapp.api.viewssets import CompanyViewSet
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter
router.register('company')


urlpatterns = [
    path('company/', include('myapp.urls', namespace='company')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
