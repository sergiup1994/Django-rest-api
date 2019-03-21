"""event_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from api import views
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()
router.register(r'match', views.MatchViewSet)

schema_view = get_schema_view(title='Sport Events')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', schema_view),
    path('event_site/', include(router.urls)),
    path('docs/', include_docs_urls(title='Sport Events'))
    
]
