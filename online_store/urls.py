from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from online_store import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('', include(('shop.urls', 'shop'), namespace='shop')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
