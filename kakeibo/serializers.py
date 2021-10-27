from rest_framework import serializers
from .models import *


class ICategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name',)
        model = ICategory


class OCategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name',)
        model = OCategory


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'memo',)
        model = Store


class IncomeSerializer(serializers.ModelSerializer):

    category_id = serializers.IntegerField(write_only=True)
    category = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'category_id', 'category', 'price', 'date', 'memo',)
        model = Income

    def get_category(self, obj):
        return obj.category.name


class OutgoSerializer(serializers.ModelSerializer):

    category_id = serializers.IntegerField(write_only=True)
    category = serializers.SerializerMethodField()
    store_id = serializers.IntegerField(write_only=True, required=False)
    store = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'category_id', 'category', 'price',
                  'date', 'store_id', 'store', 'memo',)
        model = Outgo

    def get_category(self, obj):
        return obj.category.name

    def get_store(self, obj):
        return obj.store.name if obj.store is not None else None
