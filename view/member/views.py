from django.shortcuts import render, redirect
from django.views import View

from member.models import Member
from member.serializers import MemberSerializer

# render는 페이지를 만들어 보여주는 것이고, redirect는 사용자를 다른 뷰로 이동시키는 것입니다.

class MemberJoinView(View):

    def get(self, request):
        return render(request, 'member/join.html')

    def post(self, request):
        data = request.POST
        data = {
            'member_email': data['member-email'],
            'member_password': data['member-password'],
            'member_name': data['member-name']
        }
        Member.objects.create(**data)
        return redirect('member:login')


# 만약 메인페이지에서 로그인을 누르면 html파일에 a 태그에 걸려있는 url : 'member:login'을 통해 member에 url로 이동되고
# member에 url에는 path('login/', MemberLoginView.as_view(), name='login')과 같은 메서드로 인해
# 로그인뷰가 실행됨
class MemberLoginView(View):
    def get(self, request):
        return render(request, 'member/login.html')

    def post(self, request):
        data = request.POST
        data = {
            'member_email': data['member-email'],
            'member_password': data['member-password']
        }

        # exist()를 사용하기 위해서 QuerySet 객체로 조회
        member = Member.objects.filter(**data)
        url = 'member:login'
        if member.exists():
            # 성공
            request.session['member'] = MemberSerializer(member.first()).data
            url = '/'
        return redirect(url)


class MemberLogoutView(View):
    def get(self, request):
        # 세션 내 정보 전체 초기화
        request.session.clear()

        return redirect('member:login')