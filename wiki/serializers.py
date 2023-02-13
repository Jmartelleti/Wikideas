from rest_framework.serializers import ModelSerializer
from .models import wiki


class Wikiideas(ModelSerializer):
    class Meta: 
        model= wiki
        fields = '__all__'