from django.urls import path
import ordesapp.views as ordesapp


app_name = 'ordesapp'

urlpatterns = [
    path('', ordesapp.OrderListView.as_view(), name='list'),
    path('read/<pk>/', ordesapp.OrderDetailView.as_view(), name='read'),
    path('create/', ordesapp.OrderCreateView.as_view(), name='create'),
    path('update/<pk>/', ordesapp.OrderUpdateView.as_view(), name='update'),
    path('delete/<pk>/', ordesapp.OrderDeleteView.as_view(), name='delete'),
    path('cancel/<pk>/', ordesapp.order_forming_complete, name='forming_cancel'),
    path('product/price/<int:pk>/', ordesapp.get_product_price, name='get_product_price'),
]
