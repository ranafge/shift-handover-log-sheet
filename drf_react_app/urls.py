from django.urls import path
from . import views

urlpatterns =[
    path('api/lead/', views.LeadListCreate.as_view(), name='api-lead'),
    # path('api/category/', views.CategoryListView.as_view({'get': 'list'}), name='api-category'),
    # path('api/task/', views.TrackView.as_view(), name='api-task'),
    path('api/users/', views.UserViewSet, name='user'),
    # path('api/authors/', views.AuthorViewSet.as_view(), name='authors'),
    # path('api/books/', views.BookViewSet.as_view(), name='book'),
]