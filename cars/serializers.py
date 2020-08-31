from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer
from .models import Auto


class CarSerializer(ModelSerializer):
    mark = SlugRelatedField(read_only=True, slug_field='name')
    kind = SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Auto
        fields = ['image', 'mark', 'model', 'kind', 'year_of_issue', 'vin', 'description', 'amount']
