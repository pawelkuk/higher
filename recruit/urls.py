from django.urls import path
from . import views

app_name = "api"
urlpatterns = [
    path("add-mark/", views.AddMarkView.as_view(), name="add_mark"),
    path("candidates/", views.candidates, name="candidates"),
]
