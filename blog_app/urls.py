from django.urls import path
from .views import *
urlpatterns = [
    path("blog/add/view/",BlogData.as_view()),
    path("blog/edit/del/<int:id>/",BlogView.as_view()),
]
