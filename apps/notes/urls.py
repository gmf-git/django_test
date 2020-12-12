from rest_framework import routers
from notes import views

urlpatterns = [

]
router = routers.DefaultRouter()
router.register('nodes', views.NotesViewSet, basename='nodes')
urlpatterns += router.urls
