from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[

    path('',views.blog, name='blog'),
    path("post/create/", views.PostCreateView.as_view(), name="post_create"),
    path('post/<int:pk>/',views.post_detail, name='post_detail'),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
    path('posts/api/',views.PostAPIView.as_view(),name='post-list'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('posts/api/<int:pk>/',views.PostApiDetailView.as_view(),name='post-detail')
    
]