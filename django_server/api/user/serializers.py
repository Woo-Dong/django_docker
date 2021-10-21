from .models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'username',
            'nickname', 'nickname_used',
            'email',
            'phone_number',
            'birth', 'lunar',
            'profile_img',
            'terms_agreed',
            'withdrawn'
        ]
