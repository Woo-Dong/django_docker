from django.http import JsonResponse
from .models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer
from rest_framework.decorators import action
import json


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    # permission_classes = [permissions.IsAuthenticated]
    #
    @action(methods=['get'], detail=False, permission_classes=[],
            url_path='sign_up', url_name='sign_up')
    def sign_up(self, request, *args, **kwargs):
        print(">>>> USER CREATE")

        context = {
            'success': True,
            'msg': '회원가입이 완료되었습니다.'
        }

        name = request.GET.get('name', '')
        nickname = request.GET.get('nickname', '')
        nickname_used = json.loads(request.GET.get('nickname_used', 'true'))
        phone_number = request.GET.get('phone_number', '')
        print(name, nickname, nickname_used, phone_number)

        if User.objects.filter(username=phone_number).exists():
            context['success'] = False
            context['msg'] = '존재하는 핸드폰번호입니다.'
            return JsonResponse(context)

        # dateField 의 경우 날짜 기본값이 공백으로 설정되면 안됨.
        birth = request.GET.get('birth', '1970-01-01')
        lunar = json.loads(request.GET.get('lunar', 'false'))
        profile_img = request.GET.get('profile_img', '/static/assets/img/avatar.png')
        terms_agreed = json.loads(request.GET.get('terms_agreed', 'true'))
        withdrawn = json.loads(request.GET.get('withdrawn', 'false'))

        user = User.objects.create(
            username=phone_number,
            password=phone_number,
            last_name=name,
            nickname=nickname,
            nickname_used=nickname_used,
            phone_number=phone_number,
            birth=birth,
            lunar=lunar,
            profile_img=profile_img,
            terms_agreed=terms_agreed,
            withdrawn=withdrawn
        )

        return JsonResponse(context)

    @action(methods=['get'], detail=False, permission_classes=[],
            url_path='sign_in', url_name='sign_in')
    def sign_in(self, request, *args, **kwargs):
        print(">>>> USER LOGIN")

        context = {
            'success': True,
            'msg': '로그인이 완료되었습니다.'
        }

        name = request.GET.get('name', '')
        username = request.GET.get('phone_number', '')

        if User.objects.filter(username=username).exists() is False:
            context['success'] = False
            context['msg'] = '존재하지 않은 회원정보입니다.\n회원가입을 해주세요.'
            return JsonResponse(context)

        user = User.objects.get(
            phone_number=username,
            nickname=name
        )

        if user.withdrawn:
            context['success'] = False
            context['msg'] = '회원탈퇴된 정보입니다.\naibridge@naver.com으로 문의주세요.'
            return JsonResponse(context)

        user_data = user.__dict__
        del user_data['_state']
        del user_data['password']

        context['data'] = user_data

        # from django.contrib.auth import authenticate
        # authenticate(username=username, password=username)

        return JsonResponse(context)

    # 필요한 데이터 검색 (request_code)
    # 0 -> 로그인 한 사용자의 개인정보 검색.
    # 1 -> (로그인한 ID 기준) -> 해당 사용자가 생성한 방 모두 검색.
    # 2 -> (TEST) (가계도에 사용하기 위하여) 가입된 모든 유저 리스트를 검색하여 출력..
    @action(methods=['get'], detail=False, permission_classes=[],
            url_path='search_data', url_name='search_data')
    def search_data(self, request, *args, **kwargs):

        result = {
            'success': True,
            'msg': '데이터 로딩 성공.'
        }

        request_code = int(request.GET.get('request_code', -1))
        id_ = int(request.GET.get('id', -1))

        if request_code == -1 or id_ == -1:
            result['success'] = False
            result['msg'] = '데이터 로딩 실패'
            return JsonResponse(result)
        return JsonResponse(result)

    @action(methods=['get'], detail=False, permission_classes=[],
            url_path='update_profile', url_name='update_profile')
    def update_profile(self, request, *args, **kwargs):
        result = {
            'success': True,
            'msg': '업데이트 완료되었습니다.'
        }

        id_ = request.GET.get('id', '')
        name = request.GET.get('name', '')
        birth = request.GET.get('birth', '')
        phone_number = request.GET.get('phone_number', '')

        if id_ == '':
            result['success'] = False
            result['msg'] = '잘못된 회원정보입니다. 다시 시도해주세요.'
            return JsonResponse(result)

        user = User.objects.get(id=id_)
        if name != '':
            user.last_name = name

        if birth != '':
            user.birth = birth

        if phone_number != '':
            user.username = phone_number
            user.password = phone_number
            user.phone_number = phone_number

        user.save()

        return JsonResponse(result)

    @action(methods=['get'], detail=False, permission_classes=[],
            url_path='withdrawal', url_name='withdrawal')
    def withdrawal(self, request, *args, **kwargs):
        result = {
            'success': True,
            'msg': '회원탈퇴가 처리 되었습니다.'
        }

        id_ = request.GET.get('id', '')

        if id_ == '':
            result['success'] = False
            result['msg'] = '잘못된 회원정보입니다. 다시 시도해주세요.'
            return JsonResponse(result)

        user = User.objects.get(id=id_)
        user.withdrawn = True
        user.save()

        return JsonResponse(result)
