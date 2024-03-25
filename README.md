# 1. Framework
- 라이브러리란, 개발자가 작성해놓은 코드 파일을 의미하며,
- API란, 여러 라이브러리가 모여있는 압축파일을 의미한다.
- Framework란, API가 굉장히 많이 모여져서 덩치가 커져있는 것을 의미한다.

## 1-1. Framework 장점
	개발에 필요한 구조를 이미 코드로 만들어 놓았기 때문에 실력이 부족한 개발자라 하더라도
	반쯤 완성된 상태에서 필요한 부분을 조립하는 형태의 개발이 가능하다.
	회사 입장에서는 Framework를 사용하던 일정한 품질이 보장되는 결과물을 얻을 수 있고, 
	개발자 입장에서는 완성된 구조에 자신이 밑은 서비스에 대한 코드를 개발해서 넣기 때문에
	개발 시간을 단축할 수 있다.

## 1-2. Django Framework
	파이썬으로 만들어진 오픈 소스 웹 애플리케이션 프레임워크이며,
	빠르고 쉡게 웹 사이트를 개발할 수 있는 구성 요소로 이루어진 웹 프레임워크이다.

## 1-3. Django Framework 특징
	1. MVT 소프트웨어 디자인 설계 패턴 -> MVT가 계속 반복됨 
		Model: 테이블에 저장되어 있는 데이터를 불러온 뒤 담아놓는 역할
		View: 테이블에 접근한 뒤 화면에서 사용할 Model객체를 완성시킨다.
		Templates: 클라이언트에게 보여질 화면 구성, 전달받은 Model객체를 사용한다.

	2. 강력한 ORM
		ORM(Object Relational Mapping)은 객체 관계 매핑이며,
		객체 진영과 RDB 진영의 구조 차이를 자동으로 해결해주는 기술의 총칭이다.
		오로지 객체를 중심으로 설계가 가능하며, 직접 SQL문을 작성하지 않아도
		자동으로 쿼리가 생성되어 실행된다.

	3. 자체 템플릿 지원
		HTML에서 연산이 가능하도록 도와주며, 자체 템플릿 태그가 있기 때문에
		동적인 페이지를 구성할 수 있게 해준다.
		
	4. 소스코드 변경 감지
		.py 파일의 소스코드가 변경된다면, 이를 자동으로 감지하여 서버를 재시작해준다.

	5. WAS에 종속적이지 않은 환경
		서버를 실행하지 않아도 기능별 단위 테스트가 가능하기 때문에
		버그를 줄이고 개발 시간을 단축할 수 있다.

## 1-4. Django Framework의 장점
		1. 확장성
			객체를 기억하여 재사용할 수 있는 캐싱과 코드 재사용 기능으로 인해 확장성이 좋다.

		2. 보안
			개발자가 SQL 주입, CSRF 공격 및 XSS와 같은 많은 보안 문제를 피할 수 있도록 도와준다.

		3. 기본 라이브러리를 통한 빠른 개발
			처음부터 코드를 작성하는 대신 여러 기능을 포함하는 패키지를 활용할 수 있다.

## 1-5. Django Framework의 목적
- 간단한 웹 앱을 작성하거나 Python을 필요로 하는 서비스들을 가볍게 제작하여, MSA로 나누어 개발하는 목적으로 사용된다.

<hr/>

# 2. Model
	   Django에서 models.Model이라는 추상화된 클래스를 사용하여 데이터베이스에 테이블을 정의할 수 있다.
	   models.Model을 상속받은 클래스로 구현할 수 있으며, 내부 클래스로 Meta 클래스를 선언할 수 있다.

# 2-1. Model Convention
- 모델 내 코드를 작성할 때 아래의 순서에 맞춰 작성하는 것을 권장한다.

	   1. Constant for choices
	   2. All databases Field
	   3. Custom manager attributes
	   4. class Meta
	   5. def __str__()
	   6. def save()
	   7. def get_absolute_url()
	   8. Any custom methods
	
		1. Constant for choices
		   DB에 저장할 값과 실제 화면에 보여지는 값이 다를 경우 미리 튜플 형태로 선언해 놓고 사용한다.
		   
		   CONSTANT = [
		      ('DB 저장 값', '화면 출력 값'),
		      ...
		   ]
		
		2. All databases Field
		   
		   ForeignKey(to, verbose_name, related_name, related_query_name, on_delete, null)
		   OneToOneField(to, verbose_name, related_name, related_query_name, on_delete, null)
		   ManyToManyField(to, verbose_name, related_name, related_query_name, on_delete, null)
		
		   related_name
		      역참조가 필요한 다대다 또는 일대다 관계에서 유용하게 사용된다.
		      B필드에 a객체 선언 후 참조 시 b.a로 접근할 수 있으나
		      역참조인 a.b로는 접근할 수 없다. A필드에는 b객체가 없기 때문이다.
		      _set객체를 사용하면 역참조가 가능하고 a.b_set으로 역참조가 가능하다.
		      만약 _set객체의 이름을 다른 이름으로 사용하고자 할 때 바로 related_name을 사용한다.
		
		
		   문자열
		   문자열 필드는 null=False로 하고 필수 요소가 아니라면 blank=True로 설정한다.
		   이렇게 설정하는 이유는 null과 빈 값을 "null이거나 빈 문자일 경우 빈 값이다"라고 검사할 필요 없이
		   빈 문자열인지로만 판단할 수 있게 되기 때문이다.
		
		   최대 길이 제한이 필요한 경우
		   CharField(verbose_name, max_length, choices, blank, null, default)
		
		   최대 길이 제한이 필요 없을 경우
		   TextField(verbose_name, null=False, blank=True)
		
		   정수
		   max_length를 지정하지 않고 기본적으로 byte가 정해져있다.
		
		   PositiveSmallIntegerField(verbose_name, choices, null, default)
		   SmallIntegerField(verbose_name, choices, null, default)
		   IntegerField(verbose_name, choices, null, default): 4byte
		   BigIntegerField(verbose_name, choices, null, default)
		   BooleanField(verbose_name, default): 1byte
		
		   날짜
		   auto_now_add=True
		      최초 한 번만 자동으로 필드 값을 현재 시간으로 설정한다.
		      보통 등록 날짜 항목으로 사용된다.
		
		   auto_now=True
		      객체가 변경될 때마다 자동으로 필드 값을 현재 시간으로 수정한다.
		      보통 수정된 날짜 항목으로 사용된다.
		      하지만, save()를 사용해야 적용되고 update()를 사용하면 적용되지 않는다.
		      auto_now=True처럼 사용하고 싶다면, default=timezone.now을 사용하는 것이 올바르다.
		      ※ django.utils.timezone.now으로 설정한 뒤 update할 때 마다 그 때의 now로 넣어준다.
		
		
		   DateField(verbose_name, null, default, auto_now_add, auto_now)
		   TimeField(verbose_name, null, default, auto_now_add, auto_now)
		   DateTimeField(verbose_name, null, default, auto_now_add, auto_now)
		
		3. Custom manager attributes
		   데이터베이스와 상호작용하는 인터페이스(틀)이며, model.objects 속성을 통해 사용한다.
		   Custom Manager와 Custom QuerySet을 통해 사용할 수 있으며,
		   공통적으로 사용되는 쿼리를 공통 함수로 정의할 수 있고 실제 동작을 숨길 수 있다.
		
		4. class Meta
		   Model 클래스 안에 선언되는 내부 클래스이며, 모델에 대한 기본 설정들을 변경할 수 있다.
		   Meta 클래스가 작동하기 위해서는 정해진 속성과 속성 값을 작성해야 하고,
		   이를 통해 Django를 훨씬 편하게 사용할 수 있다.
		
		   데이터 조회 시 정렬 방법 설정
			1. 오름차순
		   		ordering = ['필드명']
			2. 내림차순
		   		ordering = ['-필드명']
		
		   테이블 생성 시 이름 설정
		   	db_table = '테이블명'
		
		   테이블을 생성할 것인 지 설정
		   	abstract = False
		
		5. def __str__()
		   객체 조회 시 원하는 데이터를 직접 눈으로 확인하고자 할 때 사용하며,
		   객체 출력 시 자동으로 사용되는 메소드이다.
		   모델 필드 내에서 재정의하여 원하는 필드를 문자열로 리턴하면 앞으로 객체 출력 시 해당 값이 출력된다.
		
		6. def save()
		   모델 클래스를 객체화한 뒤 save()를 사용하면 INSERT 또는 UPDATE 쿼리가 발생한다.
		   이는 Django ORM이 save()를 구현해놨기 때문이다.
		   save() 사용 시, INSERT 또는 UPDATE 쿼리 발생 외 다른 로직이 필요할 경우 재정의할 수 있다.
		   하지만 재정의 하면, 객체를 대량으로 생성하거나 수정할 때 동작하지 않는다.
		
		7. def get_absolute_url()
		   모델에 대해서 상세보기(DetailView)를 제작한다면, redirect(모델 객체)를 통해
		   자동으로 get_absolute_url()을 호출한다.
		   추가 혹은 수정 서비스 이후 상세보기 페이지로 이동하게 된다면,
		   매번 redirect에 경로를 작성하지 않고 get_absolute_url()을 재정의해서 사용하는 것을 추천한다

















