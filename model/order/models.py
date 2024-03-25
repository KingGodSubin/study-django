from django.db import models

from member.models import Member
from model.models import Period


class Order(Period):
    members = models.ForeignKey(Member, on_delete=models.PROTECT, null=False)
    payment = models.TextField(null=False, blank=False) # 결제 수단
    price = models.BigIntegerField(null=False)  # 총 구매 가격
    delivery_address = models.TextField(null=False, blank=False)
    # 결제 완료(True), 결제 취소(False)
    status = models.BooleanField(null=False, default=True)

    class Meta:
        db_table = 'tbl_order'
        ordering = ['-id']