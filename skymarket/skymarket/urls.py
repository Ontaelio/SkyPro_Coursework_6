from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from djoser.views import UserViewSet

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import SimpleRouter, DefaultRouter

from ads.views import AdViewSet, CommentViewSet, MyAdsViewList
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


comments_router = SimpleRouter()
comments_router.register("comments", CommentViewSet, basename="ads")

router = DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register("ads", AdViewSet, basename="ads")
# router.register("ads/<ad__id>/comments", CommentViewSet, basename="ads")

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    path("api/redoc-tasks/", include("redoc.urls")),
    path('api/token/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path("api/ads/me/", MyAdsViewList.as_view()),
    path("api/", include(router.urls)),
    path("api/ads/<int:adid>/", include(comments_router.urls)),

    # path("api/", include(ads_router.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
