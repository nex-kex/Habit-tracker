from django.urls import path
from rest_framework.routers import DefaultRouter

from tracker.apps import TrackerConfig

from . import views

app_name = TrackerConfig.name


router = DefaultRouter()
router.register("habits", views.HabitViewSet, basename="habits")

urlpatterns = [
    path("habits/public/", views.PublicHabitListView.as_view(), name="public-habits"),
] + router.urls
