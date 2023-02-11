from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="Email already exists.",
            )
        ],
    )

    cpf = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="CPF already exists.",
            )
        ],
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "cpf",
            "is_active",
            "is_superuser",
            "is_staff",
            "created_at",
            "updated_at",
        ]

        read_only_fields = ["created_at", "updated_at"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    