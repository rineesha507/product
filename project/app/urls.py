from django.urls import path,include
from .views import ProductViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter
from .views import LoginAPI



router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
        path('', include(router.urls)),
        path('api/login/', LoginAPI.as_view(), name='login'), 
        

]
