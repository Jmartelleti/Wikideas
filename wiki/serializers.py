from rest_framework.serializers import ModelSerializer

from .models import Wiki


class Wikiideas(ModelSerializer):
    class Meta: 
        model= Wiki
        fields = '__all__'