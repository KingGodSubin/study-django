from django.db import transaction
from django.db.models import F
from django.test import TestCase

import cart_detail
from cart.models import Cart
from cart_detail.models import CartDetail
from member.models import Member
from product.models import Product


class CartTests(TestCase):
    # # 로그인
    # 강사님은 짱구가 멤버 테이블에 있지만 난 없음 따라서 회원가입 먼저 진행
    # 멤버 테이블에 create 해주면 될 것 같음
    # data = {
    #     'member_email': 'zzanggu@naver.com',
    #     'member_password': 'zzzz'
    # }
    # ==========================================================================================================
    # 짱구 회원가입 완료 하지만 이름이 안들어갔다.
    # Member.objects.create(**data)

    # 이름, 나이 업데이트 해줄것
    # count = Member.objects.filter(member_email='zzanggu@naver.com').update(member_name='짱구', member_age=5)
    # print(count)
    # ==========================================================================================================

    # member = Member.enabled_objects.get(**data)
    #
    # # 상품 목록
    # products = Product.sell_price_objects.all()
    #
    # # 상품 상세페이지
    # product = products[3]
    # print(product.__dict__)
    #
    # # 장바구니에 상품 추가
    #
    # # 내 장바구니 가져오기
    # my_cart = Cart.objects.filter(status=0, member=member)
    # print(my_cart.first().__dict__)
    #
    # if not my_cart.exists(): # 장바구니가 없을 때(장바구니에 상품이 하나도 없을 때)
    #     # 새로운 장바구니를 만들어서 my_cart에 담아준다.
    #     my_cart = Cart.objects.create(member=member)
    # else: # 장바구니가 존재할 때(장바구니에 추가된 다른 상품이 존재할 때)
    #     # 기존 장바구니를 my_cart에 담아준다.
    #     my_cart = my_cart.first()

    # 장바구니상세 테이블에 장바구니(물건을 시킨 회원정보가 들어가있음)와 상품과 수량을 넣어서 생성해줌
    # CartDetail.objects.create(cart=my_cart, product=product, quantity=2)

    # 장바구니 목록
    # 상품 정보, 수량
    # data = {
    #     'member_email': 'zzanggu@naver.com',
    #     'member_password': 'zzzz'
    # }

    # member = Member.enabled_objects.get(**data)

    # 회원의 이름과 그 회원의 장바구니 목록 보기 (수빈)
    # cart = Cart.objects.get(status=0, member=member)
    # cart_details = CartDetail.objects.filter(cart=cart, status=0).values('cart__member__member_name', 'product__product_name', 'quantity')
    # for cart_detail in cart_details:
    #     print(cart_detail)
    #
    # carts = CartDetail.objects.filter(status=0, cart=Cart.objects.get(member=member, status=0))
    # for cart in carts:
    #     print(cart.product.__dict__)
    #     print(cart.quantity)
    #     print("=" * 30)

    # 회원이 회원가입해서 상품을 두개 장바구니에 담고 그 장바구니에 담은 목록을 보여주는 코드를 작성하시오
    # data = {
    #     'member_email': 'soo982181@naver.com',
    #     'member_password': 'bin21813796',
    #     'member_name': '김수빈',
    #     'member_age': 27,
    # }
    # 회원가입 완료
    # Member.objects.create(**data)

    # 회원 정보 가져오기!
    # member = Member.objects.get(**data)
    # 전체 상품을 가져오기!
    # products = Product.sell_price_objects.all()
    # for product in products:
    #     print(product.__dict__)
    # 춘천 닭갈비와 간편 도시락을 장바구니에 담음 인덱스로 접근!!
    # product = products[3]

    # 내 장바구니 먼저 가져오기 -> 장바구니가 이미 있는지 없는지를 확인하기 위함
    # my_cart = Cart.objects.filter(status=0, member=member)

    # 당연히 장바구니가 없을 것임 상품을 처음 추가할테니깐
    # if not my_cart.exists():
        # 장바구니가 없다면 그 회원의 장바구니를 추가해줘야함
        # my_cart = Cart.objects.create(member=member)
    # else:
        # 장바구니가 있다면 그 장바구니에 상품을 추가해줘야하기 때문에 장바구니를 가져와야함
        # my_cart = my_cart.first()

    # 장바구니가 있는지 없는지를 확인했다면 장바구니 상세에 상품과 개수를 담아줘야함
    # CartDetail.objects.create(cart=my_cart, product=product, quantity=10)

    # 그 장바구니에 담은 목록을 보여주는 코드를 작성
    # .values('cart__member__member_name', 'product__product_name', 'product__product_price')
    # cart_details = CartDetail.objects.filter(cart=my_cart)

    # for cart_detail in cart_details:
    #     product_sell_price = cart_detail.product.product_sell_price
    #     cart_detail.product_sell_price = product_sell_price
    #     print(cart_detail.cart.member.member_name, cart_detail.product.product_name, cart_detail.quantity, cart_detail.product.product_price, cart_detail.product_sell_price)

    # 장바구니에 담긴 상품 임의로 삭제
    # 오류 발생 시 자동 롤백을 위해 사용하고,
    # 오류가 없으면 커밋된다.
    # @transaction.atomic # 메소드 전체를 하나의 트랜잭션으로 설정
    # def service(self):
    # with transaction.atomic(): # 블록 전체를 하나의 트랜잭션으로 설정
        # data = {
        #     'member_email': 'zzanggu@naver.com',
        #     'member_password': 'zzzz'
        # }
        # Cart.objects.all().update(status=0)
        # CartDetail.objects.all().update(status=0)
        # member = Member.objects.get(**data)
        # my_cart = Cart.objects.get(member=member, status=0)
        # #
        # carts = CartDetail.objects.filter(status=0, cart=my_cart)
        # #
        # cart = carts[0]
        # #
        # cart.status = -1
        # cart.save(update_fields=['status'])
        #
        # if not CartDetail.objects.filter(cart=my_cart, status=0).exists():
        #     my_cart.status = -2
        #     my_cart.save(update_fields=['status'])
    pass










