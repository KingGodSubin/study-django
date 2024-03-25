from django.shortcuts import render
from django.views import View


class MainView(View):
    # 일단 request.session['member'] 세션에 멤버가 있다면 member 변수에 가지고 와서 넣어줌
    # 세션은 서버에 저장된 공간
    def get(self, request):
        try:
            member = request.session['member']

        except KeyError:
            member = None

        return render(request, 'main.html', {"member": member})