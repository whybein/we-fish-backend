from django.urls import path
from .views      import CategoryView, ThemeView, ReviewWriteView

urlpatterns = [
    path('/category_list', CategoryView.as_view()),
    path('/theme', ThemeView.as_view()),
    path('/review_write', ReviewWriteView.as_view()),
]
