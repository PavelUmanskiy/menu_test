from django.urls import path

from .views import (
    index_view,
    profile_view,
    contacts_view,
    all_categories_view,
    category_view,
    category_object_view,
)

urlpatterns = [
    path('home/', index_view, name='index'),
    path('home/profile/', profile_view, name='profile'),
    path('home/contacts/', contacts_view, name='contacts'),
    path('home/categories/', all_categories_view, name='all_categories'),
    path('home/categories/<slug:category>/', category_view, name='category'),
    path('home/categories/<slug:category>/<slug:object>/', category_object_view,
         name='category_object'),
]
