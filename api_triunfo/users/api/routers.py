from rest_framework.routers import DefaultRouter
from api_triunfo.users.api.view_set import UserAPIview

router = DefaultRouter()

router.register(r'users',UserAPIview,basename='usuarios')

urlpatterns = router.urls