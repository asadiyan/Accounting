from rest_framework.routers import DefaultRouter

from .api import BankViewSet

router = DefaultRouter()
router.register('banks', BankViewSet, 'banks')

urlpatterns = router.urls
