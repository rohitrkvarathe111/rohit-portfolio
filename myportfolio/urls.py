"""myportfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('stockproject/', views.stockproject, name='stockproject'),
    path('wineproject/', views.wineproject, name='wineproject'),
    path('index.html', views.index, name='index'),
    path('visulaization/', views.visulaize, name='visulaization'),
    path('jobportaldetail/', views.jobportal, name='jobportaldetail'),
    path('livetradeproject/', views.livetradeproject, name='livetradeproject'),
    path('todoproject/', views.todoproject, name='todoproject'),
    path('scrapyproject/', views.scrapyproject, name='scrapyproject'),
    path('htmlproject/', views.htmlproject, name='htmlproject'),
    path('streamlitproject/', views.streamlitproject, name='streamlitproject'),

    path('', include('myadmin.urls')),

]

