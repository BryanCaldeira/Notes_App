from django.contrib import admin
from django.urls import path
from Pages import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path('',views.Main,name="main"),
	path('devop/',views.Devop,name="devop"),
	path('sem3/',views.Sem3,name="sem3"),
	path('sem4/',views.Sem4,name="sem4"),
	path('sem5/',views.Sem5,name="sem5"),
	path('sem6/',views.Sem6,name="sem6"),
	path('back/',views.Back,name="back"),
    path('csnotes6/', admin.site.urls),
]
