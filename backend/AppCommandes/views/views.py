from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models.models import *
from ..serializers.serializers import *
from ..permissions import IsSuperOrOnlyGet, OnlyGet, IsSuper


class ProduitViewSet(viewsets.ModelViewSet):
    permission_classes = [OnlyGet, IsAuthenticated]
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer


class CategorieViewSet(viewsets.ModelViewSet):
    permission_classes = [OnlyGet, IsAuthenticated]
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer


class AlerteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSuperOrOnlyGet]
    queryset = Alerte.objects.all()
    serializer_class = AlerteSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return self.queryset
        else:
            return Alerte.objects.filter(alleeMagasin__categorie__role=user.role)


class HistoryLoginViewSet(viewsets.ModelViewSet):
    permission_classes = [OnlyGet, IsAuthenticated]
    queryset = HistoryLogin.objects.all()
    serializer_class = HistoryLoginSerializer


class SupportAppViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSuper, IsAuthenticated]
    queryset = SupportApp.objects.all()
    serializer_class = SupportAppSerializer
