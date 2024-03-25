from django.db.models import F, Count
from django.test import TestCase

from member.models import Member
from post.models import Post
from reply.models import Reply


class ReplyTest(TestCase):
    # 댓글 추가
    # 로그인한 사용자의 정보를 가져오기 위한 코드
    # member_data = {
    #     'member_email': 'test5@gmail.com',
    #     'member_password': '1234'
    # }
    #
    # 멤버 table에서 email이 'test5@gmail.com'이고, password가 1234인 정보를 가져옴
    # member = Member.enabled_objects.get(**member_data)
    # 7번 게시글을 가져옴
    # post = Post.objects.get(id=7)
    #
    # 댓글을 추가하기 위한 코드
    # member에는 5번 멤버가 담겨있고, post에는 7번 게시글이 담겨져 있음
    # 따라서 reply 테이블에는 5번 회원이 7번 게시물에 작성한 댓글 테스트2로 나온다
    # reply_data = {
    #     'reply_content': '댓글 테스트2',
    #     'member': member,
    #     'post': post,
    #
    # }
    #
    # reply = Reply.objects.create(**reply_data)
    # reply.group_id = reply.id
    # reply.save()

    # 댓글 추가 (수빈)
    # 로그인한 회원 정보 가져오기
    # data = {
    #     'member_email': 'test3@gmail.com',
    #     'member_password': '1234'
    # }
    # member = Member.objects.get(**data)

    # 3번 게시물 가져오기
    # post = Post.objects.get(id=3)
    #
    # reply_data = {
    #     'reply_content': '3번 게시물에 단 댓글',
    #     'member': member,
    #     'post': post
    # }
    #
    # reply = Reply.objects.create(**reply_data)
    # reply.group_id = reply.id
    # reply.save()

    # 대댓글 3개 등록하기 (수빈)
    data = {
        'member_email': 'test4@gmail.com',
        'member_password': '1234'
    }

    member = Member.objects.get(**data)

    # 1번 게시물 가져오기
    post = Post.objects.get(id=1)
    # print(post.id)

    # 1번 게시물에 달린 댓글을 먼저 가져와야함
    reply = Reply.objects.filter(post_id=post.id, reply_depth=1)[0]
    print(reply.__dict__)
    # 대댓글 추가
    # reply_data = {
    #     'reply_content': '댓글 테스트1에 단 대댓글',
    #     여기서 멤버는 대댓글 작성자이고 위에 댓글 추가에 넣은 멤버는 댓글 작성자
    #     'member': member,
    #     'post': post,
    #     'reply_depth': 2,
    #     'group_id': reply.group_id,
    #     'reply_private_status': True
    # }

    # reply = Reply.objects.create(**reply_data)

    # replys = Reply.objects.all()
    # for reply in replys:
    #     print(reply.__dict__)

    # 대댓글 3개 등록하기
    # ※ 실행 3번으로 3개 등록하기
    # member_data = {
    #     'member_email': 'test6@gmail.com',
    #     'member_password': '1234'
    # }

    # test6@gmail.com, 1234인 회원을 가져옴
    # member = Member.objects.get(**member_data)

    # 7번 게시글 가져오기
    # post = Post.objects.get(id=7)
    # print(post.id)

    # 7번 게시글에 달린 댓글 가져오기 왜냐면 reply_depth가 1이니깐
    # reply = Reply.objects.filter(post_id=post.id, reply_depth=1)[0]
    # print(reply.id)

    # 대댓글 등록
    #     post는 7번 게시글이 들어가고
    #     member에는 6번 회원이 들어감
    #     group_id를 사용하는 이유는 댓글을 찾아서 그 댓글과 대댓글을 묶어주기 위함이다
    #     reply_depth=2를 사용하는 이유는 우선 대댓글을 추가하기 때문인데 댓글의 깊이는 1이고 대댓글은 그 댓글에 밑에 달리기 때문에
    #     깊이를 2로 설정한다 따라서 깊이가 2인 댓글들은 싹 다 깊이가 2임
    # re_reply_data = {
    #     'reply_content': '테스트 대댓글3',
    #     'post': post,
    #     'member': member,
    #     'group_id': reply.id,
    #     'reply_depth': 2,
    #     'reply_private_status': True
    # }
    #
    # re_reply = Reply.objects.create(**re_reply_data)
    # print(re_reply)
    #
    # replies = Reply.objects.filter(group_id=2)
    # for reply in replies:
    #     print(reply.get_reply_private_status_display())

    # 게시글 상세보기
    # 게시글 정보, 회원 정보, 댓글 목록, 댓글의 대댓글 목록

    # 3번 게시글의 내용과 작성자 정보를 가져온다.
    # annotate == 별칭주기
    # post = Post.objects.filter(id=3)\
    #     .annotate(member_name=F('member__member_name'))\
    #     .values(
    #     'id',
    #     'post_title',
    #     'post_content',
    #     'member_name').first()

    # 게시글에 맞는 댓글 목록
    # replies = Reply.objects.filter(post_id=post['id'], reply_depth=1)
    #
    # for reply in replies:
    #     print(reply)

    # 댓글 번호를 전달받은 뒤
    # data = {
    #     'id': 2
    # }

    # 전달받은 댓글의 대댓글을 모두 가져온다.
    # re_replies = Reply.objects.filter(group_id=data['id'], reply_depth=2)
    #
    # for re_reply in re_replies:
    #     print(re_reply)

    # 게시글을 작성한 적이 있는 회원 목록 출력
    # members = Member.objects.filter(post__isnull=False).values()
    # for member in members:
    #     print(member)

    # 대댓글을 작성한 적이 없는 회원 목록 출력
    # replies = Reply.objects.filter(reply_depth=2).values('member_id')
    # member_ids = set()
    # for reply in replies:
    #     member_ids.add(reply['member_id'])
    #
    # members = Member.objects.exclude(id__in=member_ids).values()
    # for member in members:
    #     print(member)

    # members = Member.objects.exclude(reply__reply_depth=2).values('id', 'reply')
    # for member in members:
    #     print(member)

    # 게시글 상세보기
    # 게시글 정보, 회원 정보, 댓글 목록, 댓글의 대댓글 목록

    # 3번 게시물 작성자 test14
    post = Post.objects.filter(id=3)[0]  #.values('id', 'member__member_name')[0]

    # 3번 게시물 제목, 내용, depth = 1 댓글 depth = 2 대댓글
    replies = Reply.objects.filter(post=post, reply_depth=2).values('post__post_title', 'post__post_content', 'reply_content')

    print(post)

    for reply in replies:
        print(reply)
