from rest_framework.routers import DefaultRouter

from .api import CustomerViewSet

router = DefaultRouter()
router.register('customers', CustomerViewSet, 'customers')

urlpatterns = router.urls
