from rest_framework import routers
from model.viewsets import valuationMetricsViewSet, UserViewSet

router = routers.DefaultRouter()

router.register(r'valuationMetrics', valuationMetricsViewSet)
router.register(r'users', UserViewSet)

