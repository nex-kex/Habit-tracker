from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from users.apps import UsersConfig

from . import views


app_name = UsersConfig.name


urlpatterns = [
    # token
    path("token/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="token_obtain_pair"),
]
