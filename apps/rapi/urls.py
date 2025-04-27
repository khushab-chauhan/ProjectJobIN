from django.urls import path
from apps.rapi.views import CARLISTAPI

urlpatterns = [
    path("carlistapi/", CARLISTAPI.as_view({'get': 'list', 'post': 'create'}), name="carlistapi"),
]
