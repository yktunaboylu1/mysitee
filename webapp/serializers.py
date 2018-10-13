from rest_framework import serializers
from .models import *

class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'text', 'sender', 'receiver')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'product_id', 'sender', 'sender_name', 'sender_image')

class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    image = Base64ImageField(
        max_length=None, use_url=True,
    )
    class Meta:
        model = Product
        fields = ('id', 'title', 'body', 'date', 'category', 'author', 'image', 'comments', 'price', 'location', 'featured', 'condition', 'warranty', 'shipping', 'type')

class ProductSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'date', 'price', 'image', 'featured', 'condition', 'warranty', 'shipping', 'type')

class CategSerializer(serializers.ModelSerializer):
    products = ProductSimpleSerializer(many=True, read_only=True)
    class Meta:
        model = Categ
        fields = ('id', 'cat_title', 'tagline', 'icon', 'products')

class UserProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'author', 'price', 'featured')

class UserTradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ('id', 'offered_product', 'offered_amount')

class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ('id', 'desired_product', 'offered_product', 'offered_amount', 'receiving_user', 'desired_product_title', 'offered_product_title')

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('id', 'product', 'amount', 'product_user', 'sender', 'sender_name', 'product_title')

class GlobalSearchSerializer(serializers.ModelSerializer):
   class Meta:
      model = Product
      fields = '__all__'

   def to_native(self, obj):
     serializer = ProductSerializer(obj)

     return serializer.data
