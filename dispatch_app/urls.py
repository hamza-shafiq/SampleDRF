from rest_framework.routers import DefaultRouter
from . import views, viewsets

app_name = "dispatch_app"

router = DefaultRouter()
router.register(r'user', viewsets.UserViewSets, basename='user')
router.register(r'dispatch', viewsets.DispatchViewSets, basename='dispatch')
urlpatterns = router.urls
