from rest_framework import routers
from apps.system import views

urlpatterns = [

]
router = routers.DefaultRouter()
router.register('user', views.UserViewSet, basename='user')
router.register('role', views.RoleViewSet, basename='role')
urlpatterns += router.urls
