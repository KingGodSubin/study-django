from django.db import models

from order.models import Order
from product.models import Product


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=False)  # 주문 번호
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=False)  # 주문 상품
    quantity = models.IntegerField(null=False, default=1)  # 해당 상품의 개수

    class Meta:
        db_table = 'tbl_order_detail'
        ordering = ['-id']