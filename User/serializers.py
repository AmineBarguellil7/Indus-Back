from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    isSupervisor = serializers.BooleanField(default=False)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'isSupervisor')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        is_supervisor = validated_data.pop('isSupervisor', False)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()

        if is_supervisor:
            instance.isSupervisor = True  # Corrected field name
            instance.save()

        return instance
