"""recorder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from base.views import CreateRecordingView, GetDataView, AllRecordingsView, SingleVideoView, MergeRecordingView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Screen recording API",
        default_version='v1',
        description="Screen recording API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create/', CreateRecordingView.as_view()),
    path('api/all/', AllRecordingsView.as_view()),
    path('api/save-data/<int:id>/', GetDataView.as_view()),
    path('api/merge-data/<int:id>/', MergeRecordingView.as_view()),
    path('api/<int:id>/', SingleVideoView.as_view()),
    
    
    # path('api/recording/<int:id>/', VideoRecordingsView.as_view()),
    # path('api/video/<int:id>/', SingleVideoView.as_view()),
    # path('api/stream/<int:id>/', RecordingVideoView.as_view()),





    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
