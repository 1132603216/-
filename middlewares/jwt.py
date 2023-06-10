from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from python.utils.jwt_auth import parse_payload


class JwtAuthorizationMiddleware(MiddlewareMixin):
    """
    用户需要通过请求头的方式来进行传输token，例如：
    Authorization:jwt eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NzM1NTU1NzksInVzZXJuYW1lIjoid3VwZWlxaSIsInVzZXJfaWQiOjF9.xj-7qSts6Yg5Ui55-aUOHJS4KSaeLq5weXMui2IIEJU
    """

    def process_request(self, request):
        print(request.path_info)
        white_list = ['/info/','/stay/','/post/','/delFriend/','/addFriend/','/update/','/upload/']
        # 如果是登录页面，则通过
        # if request.path_info == '/login/' \
        #         or request.path_info == '/allContent/' \
        #         or request.path_info == '/reg/' \
        #         or request.path_info == '/'\
        #         or request.path_info == '/login.html'\
        #         or request.path_info == '/stay.html'\
        #         or request.path_info == '/person.html'\
        #         or request.path_info == '/allSpeek/'\
        #         or request.path_info == '/getSpeek/'\
        #         or request.path_info == '/getStay/'\
        #         or request.path_info == '/search/':
        #     return

        if request.path_info not in white_list:
            return

        # 非登录页面需要校验token
        authorization = request.META.get('HTTP_AUTHORIZATION', '')
        if not authorization:
            return JsonResponse({"error":"无权限访问"})
        auth = authorization.split()
        # 验证头信息的token信息是否合法
        if not auth:
            return JsonResponse({})

        token = auth[1]
        # 解密
        result = parse_payload(token)
        if not result['status']:
            return JsonResponse({})
        request.userinfo = result['data']
        return
