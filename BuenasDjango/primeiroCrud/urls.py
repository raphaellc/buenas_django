from django.urls import path
from django.http import HttpResponse
from .views import PessoaCreateView, PessoaListView
from rest_framework import routers
from .views import PessoaViewSet

router = routers.DefaultRouter()
router.register(r'pessoas', PessoaViewSet)

urlpatterns = router.urls