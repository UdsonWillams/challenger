from django.urls import path

from .views import (
    ListCreateCareersView,
    PatchOrDeleteCareersView,
)

app_name = "careers"

urlpatterns = [
        path("careers/", ListCreateCareersView.as_view(), name="list-or-create-careers"),    
        path("careers/<int:pk>", PatchOrDeleteCareersView.as_view(), name="patch-or-dele-careers"),
    ]
