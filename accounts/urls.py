from rest_framework.routers import DefaultRouter

from .api import AccountViewSets

router = DefaultRouter()
router.register('account', AccountViewSets, 'account')

urlpatterns = router.urls
