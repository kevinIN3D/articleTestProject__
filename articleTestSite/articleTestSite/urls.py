from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from articles.views import HomePage
admin.autodiscover()

urlpatterns = [
    url(r'^articles/', include('articles.urls')),
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
] + [
    static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT),
]