from django.urls import path
from user.views import HelloView

urlpatterns = [
    path("", HelloView.as_view())
]