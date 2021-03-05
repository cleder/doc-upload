# urls.py
from django.urls import path
from .views import DocumentList, DocumentCreate

urlpatterns = [
    path("", DocumentList.as_view(), name="list"),
    path("add/", DocumentCreate.as_view(), name="create"),
]
