from rest_framework import routers

from .views import DreamViewSet,UserViewSet

router = routers.DefaultRouter()
router.register(r'dreams', DreamViewSet, 'Dreams')
router.register(r'get_user_info', UserViewSet, 'User')

urlpatterns = router.urls