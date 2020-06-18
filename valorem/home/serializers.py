from django.contrib.auth.models import User, Group
from rest_framework import serializers
from accounts.models import Shipment, Company


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']



class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['url', 'user', 'company_name', 'rate_increase']

class ShipmentSerializer(serializers.HyperlinkedModelSerializer):
    user_name = UserSerializer()
    company_name = CompanySerializer()
    class Meta:
        model = Shipment
        fields = ['url', 'user_name' ,'tracking_number', 'total_price', 'shipment_date', 'company_name', 'service_level', 'destination', 'ref_1', 'ref_2', 'weight']