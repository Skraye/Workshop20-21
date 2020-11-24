from ..models.models import *
from rest_framework import serializers


class MagasinSerializer(serializers.ModelSerializer):
    """
        Serializer is used to format data when post,put,get
        It take the new "object", check if it data correspond
        to the models requirement(length,unique,null...)
        Read https://www.django-rest-framework.org/api-guide/serializers/
        for better explication
    """

    class Meta:
        model = Magasin
        fields = "__all__"


class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = "__all__"


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class CategorieSerializer(serializers.ModelSerializer):

    role = serializers.CharField(source="role.name")
    produits = ProduitSerializer(source="produits", many=True, read_only=True)

    class Meta:
        model = Categorie
        fields = "__all__"


class AlleeReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlleeReserve
        fields = "__all__"


class AlleeMagasinSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlleeMagasin
        fields = "__all__"


class AlerteSerializer(serializers.ModelSerializer):
    produit = ProduitSerializer(read_only=True)
    alleeMagasin = AlleeMagasinSerializer()

    class Meta:
        model = Alerte
        fields = "__all__"


class HistoryLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryLogin
        fields = "__all__"


class SupportAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportApp
        fields = "__all__"
