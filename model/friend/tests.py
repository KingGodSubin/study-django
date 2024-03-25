from django.db.models import Q
from django.test import TestCase

from friend.models import Friend
from member.models import Member


class FriendTest(TestCase):
    pass
# data = {
#     'member_email': 'yuri@hanmail.net',
#     'member_password': 'yyyy',
#     'member_name': '유리',
#     'member_age': 5
# }
#
# Member.objects.create(**data)

# 친구 요청
# data = {
#     'member_email': 'zzanggu@naver.com',
#     'member_password': 'zzzz'
# }
#
# sender = Member.objects.get(**data)
#
# data = {
#     'member_email': 'yuri@hanmail.net'
# }
#
# receiver = Member.objects.get(member_email=data['member_email'])
#
# Friend.objects.create(sender=sender, receiver=receiver)

# 친구 요청 조건(False일 때에만 요청 가능)
# data = {
#     'member_email': 'yuri@hanmail.net'
# }
#
# receiver = Member.objects.get(member_email=data['member_email'])
#
# condition_exist = Q(receiver=receiver)
# condition_status = Q(status=1) | Q(status=0)
# condition = condition_exist & condition_status
#
# condition = Friend.objects.filter(condition).exists()
# print(condition)

# 친구 목록


# 친구 삭제
# 친구 수락
# 친구 거절