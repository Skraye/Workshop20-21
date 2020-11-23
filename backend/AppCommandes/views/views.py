from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models.models import *
from ..serializers.serializers import *
from ..permissions import IsSuperOrOnlyGet, OnlyGet, IsSuper


class CommandeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSuperOrOnlyGet, IsAuthenticated]
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            updatedCommande = serializer.save()
            newHistory = HistoryAction(
                modificationBy=request.user.email,
                modificationType=serializer.data["statutCommande"],
                commande=updatedCommande,
            )
            newHistory.save()
            if getattr(instance, "_prefetched_objects_cache", None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        return Response(serializer.errors, 400)


class HistoryActionViewSet(viewsets.ModelViewSet):
    permission_classes = [OnlyGet, IsAuthenticated]
    queryset = HistoryAction.objects.all()
    serializer_class = HistoryActionSerializer


class HistoryLoginViewSet(viewsets.ModelViewSet):
    permission_classes = [OnlyGet, IsAuthenticated]
    queryset = HistoryLogin.objects.all()
    serializer_class = HistoryLoginSerializer


class SupportAppViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSuper, IsAuthenticated]
    queryset = SupportApp.objects.all()
    serializer_class = SupportAppSerializer
