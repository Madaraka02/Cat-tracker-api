from django.urls import path
from .views import *

urlpatterns =[
    path('cats/', CatListView.as_view(), name='cats'),
    path('cats/create/', CatCreateView.as_view(), name='cats_create'),
    path('cats/<uuid:id>/edit/', CatUpdateView.as_view(), name='cat_edit'),
    path('cats/<uuid:id>/delete/', CatDeleteView.as_view(), name='cat_delete'),
    path('cats/<uuid:id>/', CatRetrieveView.as_view(), name='cat'),
]