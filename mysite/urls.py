from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("person_products/<int:person_id>/", views.person_products, name="person_products"),  # New URL pattern
    path("person_details/<int:person_id>/",views.person_details, name = "person_details"),
    path("product_details/<int:person_id>/<int:product_id>/", views.product_details, name = "product_details"),
    path('person/create/', views.create_person, name='create_person'),
    path('product/create/<int:person_id>/', views.create_product, name='create_product'),
    # other paths...
]
