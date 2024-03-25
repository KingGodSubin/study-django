from django.db.models import Q, Count
from django.test import TestCase
from random import randint

from member.models import Member
from post.models import Post


class PostTest(TestCase):
    # posts = []
    # # 랜덤한 회원을 작성자로 설정하기
    # member_queryset = Member.objects.all()
    # # 총 98개 게시글 작성하기
    # for i in range(98):
    #     post = {
    #         'post_title': f'테스트 제목{i + 1}',
    #         'post_content': f'테스트 내용{i + 1}',
    #         'member': member_queryset[randint(0, len(member_queryset) - 1)]
    #     }
    #     # 트러블 슈팅
    #     # Code: posts.append(post)
    #     # Error: AttributeError: 'dict' object has no attribute 'pk'
    #
    #     # dict객체를 Django ORM에 전달하면 정확히 인식이 안되었다.
    #     # 이를 모델 객체에 담아서 전달하니 정확이 인식되었다.
    #
    #     posts.append(Post(**post))
    #
    # Post.objects.bulk_create(posts)
    #  강사님 코드



    #  내가 연습
    # 로그인된 회원의 마이페이지에서 내가 작성한 게시글 조회하기
    # values는 딕셔너리 QuerySet을 반환
    # posts = Post.objects.filter(member__member_status=True, member_id=3).values('post_title', 'post_content')
    #
    # for post in posts:
    #     print(post)
    # member = Member.objects.get(member_status=True, id=3)
    # print(member.__dict__)
    # for post in member.post_set.all():
    #     print(post.__dict__)

    # 나이가 30 미만인 회원이 작성한 게시글 목록 조회
    # 단, 회원의 이름과 회원의 나이까지 같이 조회하기
    # 1. 정방향으로 참조
    # 시작이 어디인지가 중요함 post에서 시작해서 member 테이블까지 뽑아올꺼면 정방향 member에서 post테이블 정보를 뽑아올거면 역방향
    # posts = Post.objects.filter(member__member_age__lt=30)
    # for post in posts:
    #     print(post.post_title, post.post_content, post.member.member_name, post.member.member_age, sep=', ')

    # 2. 한번에 참조(member__member_name, member__member_age)
    # posts = Post.objects.filter(member__member_age__lt=30).values('member__member_name', 'member__member_age', 'post_title', 'post_content')
    #
    # for post in posts:
    #     print(post)

    # post : 게시물 테이블 member : 유저 테이블
    # 이름이 테스트6인 회원이 작성한 게시글 목록 조회
    # 정방향 참조
    # posts = Post.objects.filter(member__member_name='테스트6')
    # for post in posts:
    #     print(post.post_title, post.post_content, post.member.member_name, post.member.id)

    # 한번에 참조
    # posts = Post.objects.filter(member__member_name='테스트6').values('post_title', 'post_content', 'member__member_name', 'member__member_age')
    # posts = posts.order_by('-post_title')
    # for post in posts:
    #     print(post)

    # 회원이름이 테스트6이거나 회원나이가 30이상인 회원이 작성한 게시글 목록 조회
    # condition1 = Q(member__member_name='테스트6')
    # condition2 = Q(member__member_age__gt=30)
    # posts = Post.objects.filter(condition1 | condition2).values('member__member_name', 'member__member_age', 'post_title', 'post_content').order_by('-post_title')
    # for post in posts:
    #     print(post)
    # filter ---> 여러개 반환 따라서 반복문
    # values를 썻는지 --> values는 딕셔너리 QuerySet을 반환하기 때문에 .__dict__ 사용 필요 x
    # 정방향 참조
    # posts = Post.objects.filter(condition1 | condition2)
    # for post in posts:
    #     print(post.post_title, post.post_content, post.member.member_name, post.member.member_age)


    # 관리자가 작성한 게시글 목록 조회
    # 정방향 참조
    # posts = Post.objects.filter(member__member_name='관리자')
    # for post in posts:
    #     print(post.post_title, post.post_content, post.member.member_name, post.member.member_age)


    # 한번에 참조
    # posts = Post.objects.filter(member__member_name='관리자').values('post_title', 'post_content', 'member__member_name', 'member__member_age')
    # for post in posts:
    #     print(post)

    # 역방향 참조
    # members = Member.objects.get(member_name='관리자')
    # # print(members.__dict__)
    # posts = members.post_set.all()
    # for post in posts:
    #     print(post.post_title, post.post_content, post.member.member_name, post.member.member_age)

    # 게시글을 작성한 회원들중에서 게시글을 2개이상 작성한 유저 찾기
    # 게시글을 작성한 회원 중에서 게시글을 15개이상 작성한 회원 찾기
    posts = Post.objects.values(
        'member_id',
        'member__member_name',
        'member__member_age',
        'member__member_email') \
        .annotate(member_count=Count('member_id')) \
        .filter(member_count__gte=2)

    for post in posts:
        print(post)






