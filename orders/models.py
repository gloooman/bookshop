from django.db import models
# from django.db.models.signals import post_save
from products.models import Product


class OrderStatus(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Статус %s' % self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы заказа"


class Order(models.Model):
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=120, blank=True, null=True, default=None)
    status = models.ForeignKey(OrderStatus, on_delete=models.DO_NOTHING, blank=True, null=True, default=1)
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'Заказ {self.id} {self.customer_name}, общая стоимость: {self.get_total_cost()}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s' % self.product.name

    def get_cost(self):
        return self.price * self.quantity if self.is_active else 0

    class Meta:
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"

#     def save(self, *args, **kwargs):
#         price_per_item = self.product.price
#         self.price_per_item = price_per_item
#
#         self.total_price = self.nmb * self.price_per_item
#         super(ProductInOrder, self).save(*args, **kwargs)
#
#
# def product_in_order_post_save(sender, instance, *args, **kwargs):
#     order = instance.order
#     all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
#
#     order_total_price = 0
#     for item in all_products_in_order:
#         order_total_price += item.total_price
#
#     instance.order.total_price = order_total_price
#     instance.order.save(force_update=True)
#
#
# post_save.connect(product_in_order_post_save, sender=ProductInOrder)
