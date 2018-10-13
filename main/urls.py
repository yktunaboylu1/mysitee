from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from webapp import views
from webapp.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categories', views.CategView)
router.register('products', views.ProductView, base_name='products')
router.register('messages', views.MessageView)
router.register('comments', views.CommentView)
router.register(r'userproducts/(?P<author_id>[0-9]+)', views.UserProductView, base_name='userproducts')
router.register('trades', views.TradeView)
router.register('offers', views.OfferView)
router.register(r'producttrades/(?P<product_id>[0-9]+)', views.ProductTradeView, base_name='producttrades')
router.register(r'usertrades/(?P<user_id>[0-9]+)', views.UserTradeView, base_name='usertrades')
router.register(r'useroffers/(?P<user_id>[0-9]+)', views.UserOfferView, base_name='useroffers')
router.register('featured', views.FeaturedProductView, base_name='featured')

urlpatterns = [
    path('', include('webapp.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/users/', include('users.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api/rest-auth/register/', include('rest_auth.registration.urls')),
    url(r'^api/search/$', GlobalSearchList.as_view(), name="search"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
