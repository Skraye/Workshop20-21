from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes
from ..models import *


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getUser(request):
    response_data = {}
    response_data["mail"] = request.user.email
    response_data["isManager"] = request.user.is_superuser
    response_data["role"] = request.user.role
    return Response(response_data, 200)


@api_view(["GET"])
def checkOnline(request):
    return Response({}, 200)


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[-1].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


class CustomObtainAuthToken(ObtainAuthToken):
    """
        Réponse custom pour le login
        Permet de garder les logs de chaque
        identification des utilisateurs
    """

    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        print(request.data["username"])
        HistoryLogin.objects.create(
            ipAddress=get_client_ip(request),
            mail=AppUser.objects.get(username=request.data["username"]).email,
        )
        token = Token.objects.get(key=response.data["token"])
        return Response({"username": request.data["username"], "token": token.key})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getUser(request):
    return Response(response_data, 200)
