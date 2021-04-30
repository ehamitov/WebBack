from rest_framework import serializers

from api.models import Category, Product


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    image = serializers.CharField()

    def create(self, validated_data):
        category = Category.objects.create(name=validated_data.get('name'))
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProductModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'full', 'price', 'image', 'link', 'category', 'category_id')


class Product2ModelSerializer(serializers.ModelSerializer):
    # category = CategoryModelSerializer (read_only= True)
    # category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'full', 'image', 'price')


class CategoryWithProductModelSerializer(serializers.ModelSerializer):
    products = ProductModelSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'image', 'products')


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(max_length=250)
    full = serializers.CharField()
    price = serializers.IntegerField()
    category = CategoryModelSerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        products = Product.objects.create(**validated_data)
        return products

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.full = validated_data.get('full', instance.full)
        instance.save()
        return instance
