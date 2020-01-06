from django.db import models
from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from orders.forms import CartAddProductForm


class ObjDetailMixin:
    template_name = None
    model = None

    def get(self, request, id):
        obj = self.model.objects.prefetch_related(
            'product_set',
            'product_set__productimage_set',
            'product_set__genre'
        ).filter(id=id).first()
        products = []
        if obj:
            products = obj.product_set.all()
        return render(request, self.template_name, context={
            self.model.__name__.lower(): obj,
            'products': products
        })


class CartMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.productimage_set.all()
        return context