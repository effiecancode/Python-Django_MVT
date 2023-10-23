from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # farmer app urls
    path("farmer/", include("farmer.urls")),

    # consumer app urls
    path("consumer/", include("consumer.urls")),
]
