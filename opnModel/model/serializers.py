from rest_framework import serializers
from .models import valuationMetrics
from .models import Profile
from django.contrib.auth.models import User


class valuationMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = valuationMetrics
        #fields = '__all__'
        exclude = ('user',)

    def create(self, validated_data):

        return valuationMetrics.objects.create(**validated_data)

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()


        return instance

