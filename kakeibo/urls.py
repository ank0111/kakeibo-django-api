from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import *

router = SimpleRouter()
router.register('i_category', ICategoryViewSet, basename='i_category')
router.register('o_category', OCategoryViewSet, basename='o_category')
router.register('store', StoreViewSet, basename='store')
router.register('income', IncomeViewSet, basename='income')
router.register('outgo', OutgoViewSet, basename='outgo')

urlpatterns = router.urls
