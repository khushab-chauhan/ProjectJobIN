from django.urls import path
from apps.demo.views import *


urlpatterns = [
    path('carlistapi/',CARLISTAPI ,name="CARLISTAPI"),
    path('cardetailsapi/<int:id>',CARDETAILSAPI ,name="CARLISTAPI"),

]