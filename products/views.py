from products.mixins import ObjDetailMixin
from products.models import Product, Genre, Language, Author, CountryOfOrigin
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from orders.forms import CartAddProductForm


class ProductList(FormMixin, ListView):
    template_name = 'main.html'
    model = Product
    context_object_name = 'products'
    form_class = CartAddProductForm
    paginate_by = 6
    queryset = Product.objects.select_related('author')


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'id'
    queryset = Product.objects\
        .select_related('author', 'country', 'language')\
        .prefetch_related('genre', 'productimage_set')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.productimage_set.all()
        return context


class AuthorDetail(ObjDetailMixin, View):
    model = Author
    template_name = 'products/author_detail.html'


class GenreDetail(ObjDetailMixin, View):
    model = Genre
    template_name = 'products/genre_detail.html'


class LanguageDetail(ObjDetailMixin, View):
    model = Language
    template_name = 'products/language_detail.html'


class CountryDetail(ObjDetailMixin, View):
    model = CountryOfOrigin
    template_name = 'products/country_detail.html'
