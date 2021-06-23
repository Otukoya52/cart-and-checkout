from django.urls import path 
from .views import BookList, BookDetail, CartDetail, CheckoutCartView

urlpatterns = [
    path('v1/cart/checkout/', CheckoutCartView.as_view()),
    path('v1/cart/<int:pk>/', CartDetailView.as_view()),
    path('v1/book/<int:pk>/', BookDetail.as_view()),
    path('v1/book/', BookList.as_view()),
]
