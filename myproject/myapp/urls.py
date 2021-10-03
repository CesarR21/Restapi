from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('myapp/', views.AppList.as_view()),
    path('myapp/<int:pk>/',views.AppDeatil.as_view()),
    
]