from rest_framework import serializers

from spencersapp.models import Category


class catogeryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
