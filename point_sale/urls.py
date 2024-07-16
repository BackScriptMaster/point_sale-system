from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sales/', include('sales.urls')),
    path('clients/', include('clients.urls')),
    path('products/', include('products.urls'))
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)