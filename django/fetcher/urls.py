from django.urls import path
from fetcher.views import *


urlpatterns = [
    path("items", get_items, name="get-items"),
]
