from django.contrib.auth import get_user_model
from rest_framework import serializers
from directory.api.fields import SameCompanySlugRelatedField
from django.contrib.auth import password_validation, authenticate

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    reports_to = SameCompanySlugRelatedField(
        relation_field="company",
        slug_field="pk",
        queryset=User.objects.all(),
        allow_null=True,
        required=False
    )
    company = serializers.SlugRelatedField(
        slug_field='pk',
        read_only=True
    )

    class Meta:
        model = User
        fields = [
            'pk',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'reports_to',
            'company',
        ]

        read_only_fields = [
            "pk"
        ]



class UserLoginSerializer(serializers.ModelSerializer):

    # Campos que vamos a requerir
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    # Primero validamos los datos
    def validate(self, data):

        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Las credenciales no son válidas')

        # Guardamos el usuario en el contexto para posteriormente en create recuperar el token
        self.context['user'] = user
        return data

    def create(self, data):
        """Generar o recuperar token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key