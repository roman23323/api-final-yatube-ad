from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework.routers import DefaultRouter
from .views import (
    FollowListCreateView,
    PostViewSet,
    CommentViewSet,
    GroupViewSet
)

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/', include([
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),
    # Djoser endpoints (users, token management)
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('follow/', FollowListCreateView.as_view()),
    path('posts/<int:post_id>/comments/',
        CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('posts/<int:post_id>/comments/<int:pk>/',
        CommentViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        })),
    path('', include(router.urls)),

    ])),
]
