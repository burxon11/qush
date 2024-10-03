from rest_framework import serializers

from menyu.models import Menyu


class MenyuListSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Menyu
        fields = '__all__'