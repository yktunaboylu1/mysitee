# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.conf import settings

class Categ(models.Model):
    cat_title = models.CharField(max_length = 140)
    tagline = models.CharField(max_length = 140, null=True)
    icon = models.ImageField(max_length=100, upload_to='categories', default='noimage.jpg')

    def __str__(self):
        return self.cat_title

class Product(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Categ, on_delete=models.CASCADE, related_name="products")
    image = models.ImageField(max_length=100, upload_to='product', default='noimage.jpg')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(default=0)
    location = models.CharField(max_length = 140, default='')
    featured = models.BooleanField(default=False)
    warranty = models.BooleanField(default=False)
    shipping = models.BooleanField(default=False)
    condition = models.CharField(max_length = 140, default='new')
    type = models.CharField(max_length = 140, default='sell')

    def __str__(self):
        return self.title

class Message(models.Model):
    text = models.CharField(max_length = 140)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="mes_sender", null=True)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="mes_receiver", null=True)

    def __str__(self):
        return self.text

class Comment(models.Model):
    text = models.CharField(max_length = 140)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments", null=True)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="com_sender", null=True)
    sender_name = models.CharField(max_length = 140, default='')
    sender_image = models.CharField(max_length = 140, default='noimage.jpg')

    def __str__(self):
        return self.text

class Trade(models.Model):
    desired_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="desired_product", null=True)
    offered_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="offered_product", null=True)
    offered_amount = models.IntegerField()
    receiving_user = models.IntegerField(default=0)
    desired_product_title = models.CharField(max_length = 140, default='')
    offered_product_title = models.CharField(max_length = 140, default='')

    def __str__(self):
        return self.offered_product.title + ' offered for ' + self.desired_product.title + ' with difference of ' + str(self.offered_amount)

class Offer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="for_product", null=True)
    amount = models.IntegerField()
    product_user = models.IntegerField(default=0)
    sender = models.IntegerField(default=0)
    sender_name = models.CharField(max_length = 140, default='')
    product_title = models.CharField(max_length = 140, default='')

    def __str__(self):
        return 'Offer for ' + self.product.title + ' at ' + str(self.amount)
