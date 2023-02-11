from django.urls import path
from . import views

urlpatterns = [
    path("orders/", views.OrderView.as_view()),
    path("orders/<str:order_id>/", views.OrderDetailView.as_view()),
]
