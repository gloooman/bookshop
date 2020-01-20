from django.urls import path
from products.views import *


urlpatterns = [
    path('', ProductList.as_view(), name='product_list_url'),
    path('products/<int:id>/', ProductDetail.as_view(), name='product_detail_url'),
    path('products/author/<int:id>/', AuthorDetail.as_view(), name='author_detail_url'),
    path('products/genre/<str:id>/', GenreDetail.as_view(), name='genre_detail_url'),
    path('products/language/<str:id>/', LanguageDetail.as_view(), name='language_detail_url'),
    path('products/country/<str:id>/', CountryDetail.as_view(), name='country_detail_url'),
    path('products/search/', Search.as_view(), name='search_url'),
]

