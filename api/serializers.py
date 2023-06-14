from rest_framework import serializers

from .models import Test, IQ, EQ
from .services import find_test


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('login',)


class IQSerializer(serializers.ModelSerializer):
    login = serializers.CharField(read_only=True)

    class Meta:
        model = IQ
        fields = ('score', 'login')

    def create(self, validated_data):
        validated_data['test'] = find_test(self.context['request'].data)
        return IQ.objects.create(**validated_data)


class EQSerializer(serializers.ModelSerializer):
    login = serializers.CharField(read_only=True)
    letters = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = EQ
        fields = ('letters', 'login',)

    def validate(self, attrs):
        letters = attrs.get('letters')
        if len(set(letters)) != 5:
            raise serializers.ValidationError({'letters': 'Field letters must contain exactly 5 unique elements.'})
        return attrs

    def create(self, validated_data):
        validated_data['letters'] = ','.join(validated_data.pop('letters'))
        validated_data['test'] = find_test(self.context['request'].data)
        return EQ.objects.create(**validated_data)
