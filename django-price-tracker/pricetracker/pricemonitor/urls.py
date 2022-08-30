from django.urls import path, include
from . import views

# tu pewnie dodać home, log in, log out itp

urlpatterns = [
    path('service/list/', views.ServiceList.as_view(), name='servicelist'),
    path('service/create/', views.ServiceCreate.as_view(), name='servicecreate'),
    path('service/update/<pk>/', views.ServiceUpdate.as_view(), name='serviceupdate'),
    path('service/delete/<pk>/', views.ServiceDelete.as_view(), name='servicedelete'),
    path('product/list/', views.ProductList.as_view(), name='productlist'),
    path('product/create/', views.ProductCreate.as_view(), name='productcreate'),
    path('product/update/<pk>/', views.ProductUpdate.as_view(), name='productupdate'),
    path('product/delete/<pk>/', views.ProductDelete.as_view(), name='productdelete'),
    path('serviceproduct/list/', views.ServiceProductList.as_view(), name='serviceproductlist'),
    path('servicepproduct/create/', views.ServiceProductCreate.as_view(), name='serviceproductcreate'),
    path('serviceproduct/update/<pk>/', views.ServiceProductUpdate.as_view(), name='serviceproductupdate'),
    #path('serviceproduct/delete/<pk>', views.ServiceProductDelete.as_view(), name='serviceproductdelete'),

]



