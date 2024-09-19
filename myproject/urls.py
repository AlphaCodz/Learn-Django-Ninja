from django.contrib import admin
from django.urls import path
from .api import api
from basic.api import basic_router
from ninja import NinjaAPI

api = NinjaAPI()

api.add_router("/user", basic_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls)
]
