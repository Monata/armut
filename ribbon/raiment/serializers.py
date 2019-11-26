from rest_framework import serializers
from raiment.models import Item,Packlist,Folder,FolderHas


class ItemSerializer(serializers.ModelSerializer):
    # to convert django models to JSON
    class Meta:
        model = Item
        fields = '__all__'  # ('type','color_tag','brand')


class PacklistSerializer(serializers.ModelSerializer):
    # to convert django models to JSON
    class Meta:
        model = Packlist
        fields = '__all__'  # (date,fid)


class FolderHasSerializer(serializers.ModelSerializer):
    # to convert django models to JSON
    class Meta:
        model = FolderHas
        fields = '__all__'

class FolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Folder
        fields = '__all__'
