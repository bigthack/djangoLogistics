from django.urls import path, include

from . import views
from django.views.generic.base import TemplateView
from home import views as view
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', view.UserViewSet)
router.register(r'groups', view.GroupViewSet)
router.register(r'companies', view.CompanyViewSet)
router.register(r'shipments', view.ShipmentViewSet)

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),    
    path('profile/', views.index , name='profile'), 
    path('profile/add_shipment', view.get_shipment, name='add_shipment'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]