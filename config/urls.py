



from django.contrib import admin
from django.urls import path,include
from django.conf import settings # setting.py ni import qildik
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions







schema_view = get_schema_view(
    openapi.Info(
        title="Episyche Technologies",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('accountapp.urls')),
    path('letter/',include('letterapp.urls')),
    path('letterinstruction/',include('letterinstructionapp.urls')),
    path('mainletter/',include('mainletter.urls')),
    path('signedletter/',include('signedletter.urls')),

    path('tinymce/', include('tinymce.urls')),
    
    
    path('docs/',schema_view.with_ui('swagger',cache_timeout=0),name='schema-swagger-ui'),
    path("__debug__/", include("debug_toolbar.urls")),
]

if settings.DEBUG==True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


