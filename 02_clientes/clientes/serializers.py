from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError(
                {"cpf": "Número de cpf inválido."}
            )

        if not nome_valido(data['nome']):
            raise serializers.ValidationError(
                {"nome": "Não inclua números neste campo."}
            )

        if not rg_valido(data['rg']):
            raise serializers.ValidationError(
                {"rg": "O Rg deve ter 9 digitos."}
            )

        if not celular_valido(data['celular']):
            raise serializers.ValidationError(
                {"celular":
                    "O número do celular deve seguir o padrão: (11) 98888-8888."}
            )

        return data
