from django.urls import path
import backend.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:short_link>', views.redirect_original),
    path('makeshort/', views.shorten_url)
]
