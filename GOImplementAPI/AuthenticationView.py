import ldap
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.status import (HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK)
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


class Authentication(APIView):
    # def post(self, request, format=None):
    #     username=request.data["username"]
    #     password=request.data["password"]
    #     base_dn= "dc=ingrnet,dc=com"
    #     conn = ldap.initialize('ldap://ingrnet.com')
    #     conn.set_option(ldap.OPT_REFERRALS, 0)
    #     try:
    #         if (username != "" and username is not None) and (password != "" and password is not None):
    #             result=conn.simple_bind_s(username, password)
    #             userInfo = conn.search_s(base_dn, ldap.SCOPE_SUBTREE, 'userPrincipalName=' + username)
    #             z = userInfo[0]
    #             x = z[0]
    #             y = z[1]
    #
    #             mail=y["mail"][0].decode('utf-8')
    #             try:
    #                 u = User.objects.get(email=mail)
    #                 token, _ = Token.objects.get_or_create(user=u)
    #             except User.DoesNotExist:
    #                 return Response("You do not have the access to this application.Please contact the administrator",status=HTTP_404_NOT_FOUND)
    #
    #         else:
    #             return Response("user name or password should not be empty",status=HTTP_400_BAD_REQUEST)
    #     except ldap.INVALID_CREDENTIALS:
    #             return Response("Invalid Credentials",status=HTTP_400_BAD_REQUEST)
    #     return Response({'token': token.key},
    #                     status=HTTP_200_OK)
