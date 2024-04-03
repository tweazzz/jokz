from .models import *
from django.utils.translation import gettext_lazy as _
from djoser.serializers import TokenCreateSerializer
from rest_framework import serializers
from djoser.serializers import TokenSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers
from django.utils.translation import gettext as _
from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from .models import PasswordResetToken

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'phone_num', 'photo' , 'password')
        extra_kwargs = {
            'username': {'required': False}
        }

    def validate(self, data):
        password = data.get('password')
        if not password and self.instance is None:
            raise serializers.ValidationError("Password is required")
        return data

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save(update_fields=['password'])
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance = super().update(instance, validated_data)
        if password:
            instance.set_password(password)
            instance.save(update_fields=['password'])
        return instance


class UserMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'phone_num', 'photo')


class CustomUserCreateSerializer(DjoserUserCreateSerializer):

    class Meta(DjoserUserCreateSerializer.Meta):
        fields = DjoserUserCreateSerializer.Meta.fields + ('phone_num',)

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        return validated_data

    def create(self, validated_data):
        user = super().create(validated_data)
        user.is_active = False
        user.save()
        return user


from djoser.serializers import TokenCreateSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import serializers

class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = ('auth_token',)

class CustomTokenCreateSerializer(TokenCreateSerializer):
    def create(self, validated_data):
        user = validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return token

    def validate(self, attrs):
        password = attrs.get("password")
        username = attrs.get("username")
        params = {"username": username}
        self.user = authenticate(
            request=self.context.get("request"), **params, password=password
        )
        if not self.user:
            self.user = User.objects.filter(**params).first()
            if self.user and not self.user.check_password(password):
                self.fail("invalid_credentials", detail=_("Invalid login or password"))

        if self.user and self.user.is_active:
            return attrs

        self.fail("invalid_credentials", detail=_("Invalid login or password"))

    def to_representation(self, instance):
        return TokenSerializer(instance).data


# class PasswordResetTokenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PasswordResetToken
#         fields = ['email','code', 'is_active']

class PasswordResetVerifySerializer(serializers.Serializer):
    code = serializers.CharField(max_length=4, required=True)
    email = serializers.EmailField()




class UniversitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universities
        fields = '__all__'


class AvailableUniversitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universities
        fields = ['id','name', 'logo', 'country', 'city','rating_by_country']

class ProffessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proffessions
        fields = '__all__'


class InternshipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internships
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'