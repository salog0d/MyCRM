from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("person_products/<int:person_id>/", views.person_products, name="person_products"),  # New URL pattern
    # other paths...
]
