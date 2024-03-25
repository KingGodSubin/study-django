from django.db import models
from django.utils import timezone

class EnableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=True)

class Period(models.Model):
    created_date = models.DateTimeField(null=False, auto_now_add=True)
    updated_date = models.DateTimeField(null=False, default=timezone.now)
    # 역참조 시 위에 선언한 Manager가 사용된다.
    # 보통 무언가를 하고 싶을 때 Member.objects.all <- 이런식으로 가져온다
    # 하지만 역참조 시 member.post_set 이런식으로 가져오거나 한번에 참조할 시 member__member_table 이런식으로 가져오기 때문에
    # 컴파일러가 무조건 위에 있는걸 실행 하기 때문에 objects = models.Manager() 얘를 위에 써준다
    objects = models.Manager()
    enabled_objects = EnableManager()

    class Meta:
        abstract = True