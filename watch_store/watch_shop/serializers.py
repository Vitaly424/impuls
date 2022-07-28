from django.utils.text import slugify
from rest_framework import serializers
from .models import Brand, SubBrand, Product


class BrandListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ('title_brand', 'description_brand', 'logo_brand', 'country_brand')


class BrandDetailSerializer(serializers.ModelSerializer):

    subbrands = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title_subbrand'
        )
    products = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title_product'
        )

    class Meta:
        model = Brand
        fields = ('title_brand', 'description_brand', 'subbrands', 'products')

        lookup_field = 'slug_brand'
        extra_kwargs = {
            'url': {'lookup_field': 'slug_brand'}
        }


class CRUDBrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ('title_brand', 'description_brand', 'logo_brand', 'hidden_brand', 'country_brand')

    def create(self, validated_data):
        validated_data['slug_brand'] = slugify(validated_data['title_brand'])
        return Brand.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance.slug_brand = validated_data.get('slug_brand', instance.slug_brand)
        instance.title_brand = validated_data.get('title_brand', instance.title_brand)
        instance.description_brand = validated_data.get('description_brand', instance.description_brand)
        instance.logo_brand = validated_data.get('logo_brand', instance.logo_brand)
        instance.hidden_brand = validated_data.get('False', instance.hidden_brand)
        instance.country_brand = validated_data.get('country_brand', instance.country_brand)
        instance.save()
        return instance

    lookup_field = 'slug_brand'
    extra_kwargs = {
        'url': {'lookup_field': 'slug_brand'}
    }



