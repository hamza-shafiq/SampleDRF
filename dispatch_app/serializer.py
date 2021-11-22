from rest_framework import serializers
from .models import Dispatch, User


class DispatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispatch
        fields = ('user', 'short_code')

    def create(self, validated_data):
        return Dispatch.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.short_code = validated_data.get('short_code', instance.email)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'phone', 'email')

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance
