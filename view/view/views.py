from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView


# 학생의 번호, 국어, 영어, 수학 점수를 전달받은 뒤
# 총점과 평균을 화면에 출력한다.

# form태그는 get방식을 사용한다.
# 출력 화면에서 다시 입력화면으로 돌아갈 수 있게 한다.

# 입력: product/student/register.html
# 출력: product/student/result.html

class StudentRegisterFormView(View):
    def get(self, request):
        return render(request, 'task/student/register.html')


class StudentRegisterView(View):
    def get(self, request):
        data = request.GET
        data = {
            'id': data['id'],
            'kor': int(data['kor']),
            'eng': int(data['eng']),
            'math': int(data['math'])
        }

        total = data['kor'] + data['eng'] + data['math']
        average = round(total / 3, 2)

        return redirect(f'/student/result?total={total}&average={average}')


class StudentResultView(View):
    def get(self, request):
        context = {
            'total': request.GET['total'],
            'average': request.GET['average']
        }
        return render(request, 'task/student/result.html', context)

# 회원의 이름과 나이를 전달받는다.
# 전달받은 이름과 나이를 아래와 같은 형식으로 변경시킨다.
# "홍길동님은 20살!"
# 결과 화면으로 이동한다.

# 이름과 나이 작성: product/member/register.html
# 결과 출력: product/member/result.html

class MemberRegisterFormView(View):
    def get(self, request):
        return render(request, 'task/member/register.html')

class MemberRegisterView(View):
    def get(self, request):
        data = request.GET
        return redirect(f'/member/result?name={data["name"]}&age={data["age"]}')

class MemberResultView(View):
    def get(self, request):
        context = {
            'name': request.GET['name'],
            'age': request.GET['age']
        }
        return render(request, 'task/member/result.html', context)


# # 동물의 이름, 나이, 종류, 건강상태를 입력받고
# # 이름 + 종 + 나이를 합쳐서 뒤에 건강상태를 붙여주세요
# # ex) "뽀삐 강아지 14살 아파요!"
# # 결과 화면으로 이동한다.
# # get 방식이던 post 이던 상관없음
# # 입력: product/animal/register.html
# # 출력: product/animal/result.html
class AnimalRegisterView(View):
    def get(self, request):
        return render(request, 'task/animal/register.html')
    def post(self, request):
        data = request.POST
        data = {
            'name': data['animal-name'],
            'age': data['animal-age'],
            'species': data['animal-species'],
            'condition': data['animal-condition'],

        }
        result = f'{data["name"]} {data["species"]} {data["age"]}살 {data["condition"]}'
        return redirect(f'/animal/result?result={result}')

class AnimalResultView(View):
    def get(self, request):
        data = request.GET
        context = {'result': data['result']}
        return render(request, 'task/animal/result.html', context)


# 상품 정보
# 번호, 상품명, 가격, 재고
# 상품 1개 정보를 REST 방식으로 설계한 뒤
# 화면에 출력하기
# 예시)
# product/1
# product/product/product.html
class ProductDetailView(View):
    def get(self, request):
        return render(request, 'task/product/product.html')


class ProductDetailAPI(APIView):
    def get(self, request, product_id):
        data = {
            'id': product_id,
            'product_name': '마우스',
            'product_price': 50000,
            'product_stock': 50
        }
        return Response(data)
