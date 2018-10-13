# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Q
from .models import *
from rest_framework import viewsets, generics
from .serializers import *

def index(request):
    products = Product.objects.all()
    return render(request, 'webapp/home.html', {})

class CategView(viewsets.ModelViewSet):
    queryset = Categ.objects.all()
    serializer_class = CategSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class FeaturedProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all().filter(featured = True)
    serializer_class = ProductSerializer

class MessageView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UserProductView(viewsets.ModelViewSet):
    serializer_class = UserProductSerializer
    def get_queryset(self):
        author_id = self.kwargs['author_id']
        products = Product.objects.filter(author=author_id)
        return products

class TradeView(viewsets.ModelViewSet):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer

class ProductTradeView(viewsets.ModelViewSet):
    serializer_class = TradeSerializer
    def get_queryset(self):
        product_id = self.kwargs['product_id']
        trades = Trade.objects.filter(desired_product=product_id)
        return trades

class UserTradeView(viewsets.ModelViewSet):
    serializer_class = TradeSerializer
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user_trades = Trade.objects.filter(receiving_user=user_id)
        return user_trades

class OfferView(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class UserOfferView(viewsets.ModelViewSet):
    serializer_class = OfferSerializer
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user_offers = Offer.objects.filter(product_user=user_id)
        return user_offers

class GlobalSearchList(generics.ListAPIView):
   serializer_class = GlobalSearchSerializer

   def get_queryset(self):
      query = self.request.query_params.get('query', None)
      category = self.request.query_params.get('category', None)
      location = self.request.query_params.get('location', None)

      if category == '0':
        all_results = Product.objects.filter(Q(title__icontains=query) | Q(body__icontains=query)).filter(Q(location__icontains=location))
      else:
        all_results = Product.objects.filter(Q(title__icontains=query) | Q(body__icontains=query)).filter(Q(location__icontains=location)).filter(Q(category=category))

      return all_results
