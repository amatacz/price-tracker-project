from django.urls import path, include
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView


urlpatterns = [
    path('', views.home_view, name='home'),
    path('home/', views.home_view, name='home'),
    path('service/list/', views.ServiceList.as_view(), name='servicelist'),
    path('service/create/', views.ServiceCreate.as_view(), name='servicecreate'),
    path('service/update/<pk>/', views.ServiceUpdate.as_view(), name='serviceupdate'),
    path('service/delete/<pk>/', views.ServiceDelete.as_view(), name='servicedelete'),
    path('service/detail/<pk>', views.ServiceDetail.as_view(), name='servicedetail'),
    path('product/list/', views.ProductList.as_view(), name='productlist'),
    path('product/create/', views.ProductCreate.as_view(), name='productcreate'),
    path('product/update/<pk>/', views.ProductUpdate.as_view(), name='productupdate'),
    path('product/delete/<pk>/', views.ProductDelete.as_view(), name='productdelete'),
    path('product/detail/<pk>/', views.ProductDetail.as_view(), name='productdetail'),
    path('serviceproduct/list/', views.ServiceProductList.as_view(), name='serviceproductlist'),
    path('servicepproduct/create/<service_id>', views.ServiceProductCreate.as_view(), name='serviceproductcreate'),
    path('serviceproduct/update/<pk>/', views.ServiceProductUpdate.as_view(), name='serviceproductupdate'),
    path('serviceproduct/delete/<pk>', views.ServiceProductDelete.as_view(), name='serviceproductdelete'),
    path('register/', views.signUp.as_view(), name='register'),
    path('login/', views.loginView.as_view(), name='login'),
    path('logout/', views.logoutView.as_view(), name='logout'),
    path('reset-password/', PasswordResetView.as_view(), name='reset_password'),
    path('reset-password/done/', PasswordResetDoneView.as_view(), name='reset_password_done'),
    path('reset-password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='reset_password_confirm'),
]



