from django.urls import path
import backend.views as views

urlpatterns = [
    path('<slug:short_link>', views.redirect_original),
]
