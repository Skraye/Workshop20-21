from ..models.models import *
from rest_framework import serializers


class CommandeSerializer(serializers.ModelSerializer):
    """
        Serializer is used to format data when post,put,get
        It take the new "object", check if it data correspond
        to the models requirement(length,unique,null...)
        Read https://www.django-rest-framework.org/api-guide/serializers/
        for better explication
    """

    class Meta:
        model = Commande
        fields = "__all__"


class HistoryActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryAction
        fields = "__all__"


class HistoryLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryLogin
        fields = "__all__"


class SupportAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportApp
        fields = "__all__"
