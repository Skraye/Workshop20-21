from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

router = routers.DefaultRouter()
router.register(r"produits", ProduitViewSet)
router.register(r"categories", CategorieViewSet)
router.register(r"historique-login", HistoryLoginViewSet)
router.register(r"support-app", SupportAppViewSet)

urlpatterns = [
    path("user/", getUser, name="getuser"),
    path("check-online/", checkOnline, name="checkonline"),
    path("api-token-auth/", CustomObtainAuthToken.as_view()),
]


urlpatterns += router.urls
