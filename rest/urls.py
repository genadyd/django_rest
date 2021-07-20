from django.urls import path, include
from .views import categories_views as cat_views
from .views import products_view as prod_views

urlpatterns = [
    # print some plain text or html without "view"

    path('categories/', cat_views.CategoriesListView.as_view()),
    path("categories/<int:ct_id>/", cat_views.CategoryGetDetails.as_view()),
    path('products/', prod_views.ProductsListView.as_view()),
    path('products/<int:prod_id>/', prod_views.ProductGetDetails.as_view()),
]
