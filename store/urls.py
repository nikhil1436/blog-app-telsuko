from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('signup/', views.signup),                 # Register
    path('token/', TokenObtainPairView.as_view()), # Login - Get JWT
    path('token/refresh/', TokenRefreshView.as_view()),

    path('products/', views.products),             # GET + POST
    path('cart/', views.my_cart),                  # View Cart
    path('cart/add/', views.add_to_cart),          # Add to Cart
]
