"""
URL configuration for view project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from main.views import MainView
from view import settings
from view.views import StudentRegisterView, StudentResultView, StudentRegisterFormView, MemberRegisterFormView, \
    MemberRegisterView, MemberResultView, AnimalRegisterView, AnimalResultView, ProductDetailAPI, ProductDetailView

# 맨처음에 python manage.py runserver하면 view에 urls.py 파일이 실행되는데
# http://127.0.0.1:8000/를 콘솔창에 돌려주는데 아무것도 없으니 3번째줄로 가서 메인뷰가 실행됨
# 메인뷰로 가야함
urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/', include('member.urls')),
    path('post/', include('post.urls')),
    path('student/register/form', StudentRegisterFormView.as_view(), name='student-register-form'),
    path('student/register/', StudentRegisterView.as_view(), name='student-register'),
    path('student/result/', StudentResultView.as_view(), name='student-result'),
    path('member/register/form', MemberRegisterFormView.as_view(), name='member-register-form'),
    path('member/register/', MemberRegisterView.as_view(), name='member-register'),
    path('member/result/', MemberResultView.as_view(), name='member-result'),
    path('animal/register/', AnimalRegisterView.as_view(), name='animal-register'),
    path('animal/result/', AnimalResultView.as_view(), name='animal-result'),
    path('', MainView.as_view()),
    path('products/', include('product.urls')),
    # path('products/', ProductDetailView.as_view(), name='product'),
    # path('products/<int:product_id>/', ProductDetailAPI.as_view(), name='product-api'),
]

# 파일 업로드 시의 경로를 따로 추가함
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)












