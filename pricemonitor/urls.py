from django.urls import path, include
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('home/', views.home_view, name='home'),
    
    # Service URLs
    path('service/list/', views.ServiceList.as_view(), name='servicelist'),
    path('service/create/', views.ServiceCreate.as_view(), name='servicecreate'),
    path('service/update/<pk>/', views.ServiceUpdate.as_view(), name='serviceupdate'),
    path('service/delete/<pk>/', views.ServiceDelete.as_view(), name='servicedelete'),
    path('service/detail/<pk>', views.ServiceDetail.as_view(), name='servicedetail'),
    
    # Product URLs
    path('product/list/', views.ProductList.as_view(), name='productlist'),
    path('product/create/', views.ProductCreate.as_view(), name='productcreate'),
    path('product/update/<pk>/', views.ProductUpdate.as_view(), name='productupdate'),
    path('product/delete/<pk>/', views.ProductDelete.as_view(), name='productdelete'),
    path('product/detail/<pk>/', views.ProductDetail.as_view(), name='productdetail'),

    
    path('product/list/<pk>/', views.ProductsInServiceProduct.as_view(), name='productslist'),
    path('serviceitems/list/<pk>/', views.ServiceItemsList.as_view(), name='serviceitemslist'),

    # ServiceProduct URLs
    path('serviceproduct/list/', views.ServiceProductList.as_view(), name='serviceproductlist'),
    path('serviceproduct/create/', views.ServiceProductCreate.as_view(), name='serviceproductcreate'),
    path('serviceproduct/update/<pk>/', views.ServiceProductUpdate.as_view(), name='serviceproductupdate'),
    path('serviceproduct/delete/<pk>/', views.ServiceProductDelete.as_view(), name='serviceproductdelete'),
    path('serviceproduct/detail/<pk>', views.ServiceProductDetail.as_view(), name='serviceproductdetail'), 

    # UserServiceProduct URLs
    path('watchserviceproduct/<pk>', views.UserServiceProductCreate.as_view(), name='watchserviceproduct'),
    path('deleteserviceproduct/<pk>', views.UserServiceProductDelete.as_view(), name='useserviceproductdelete'),
    path('userserviceproduct/list/', views.UserServiceProductList.as_view(), name='userserviceproductlist'),

    # Registration and user profile URLs
    path('activate/<uidb64>/<token>/', views.ActivateAccount.as_view(), name='activate'),
    path('register/', views.signUp.as_view(), name='register'),
    path('login/', views.loginView.as_view(), name='login'),
    path('logout/', views.logoutView.as_view(), name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "reset_password.html"), name ='reset_password'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = "password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "password_reset_done.html"), name ='password_reset_complete'),
    path('profile/', views.UserProfileView.as_view(), name="profile"),
    path('profile/update/', views.UserUpdateView.as_view(), name="userupdate"),
    path('profile/delete/<pk>/', views.UserDeleteView.as_view(), name="userdelete"),
]



