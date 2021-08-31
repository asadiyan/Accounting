from rest_framework.routers import DefaultRouter

from .api import HistoryViewSet

router = DefaultRouter()
router.register('histories', HistoryViewSet, 'histories')

urlpatterns = router.urls
