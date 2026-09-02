from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
]

# DEBUG True বা False যাই হোক না কেন, মিডিয়া ফাইল শো করবে
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)