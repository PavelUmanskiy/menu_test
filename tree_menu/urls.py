from django.urls import path

from .views import (
    index_view,
    category_view,
    category_object_view,
)

urlpatterns = [
    path('home/', index_view, name='index'),
    path('home/profile/', index_view, name='profile'),
    path('home/contacts/', index_view, name='contacts'),
    path('home/categories/', index_view, name='all_categories'),
    path('home/categories/<slug:category>/', category_view, name='category'),
    path('home/categories/<slug:category>/<int:pk>/', category_object_view,
         name='category_object'),
    path('sc_1/', index_view, name='sc_1')
]
