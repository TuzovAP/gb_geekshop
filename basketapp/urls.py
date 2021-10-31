from django.urls import path, include
from basketapp import views as basket
# from basketapp.views import views as basket

app_name = 'basketapp'

urlpatterns = [
    path('', basket.basket, name='basket'),
    path('add/<int:pk>/', basket.add, name='add'),
    path('remove/<int:pk>/', basket.remove, name='remove'),
]