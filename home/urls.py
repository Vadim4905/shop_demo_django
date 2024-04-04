from django.urls import path,include
from . import views

urlpatterns = [
    path('products/', views.get_all_products,name='products'),
    path('product/<int:pk>', views.get_product,name='product-detail'),
    path('review/create/<int:product_id>',views.review_form,name='review-form')
]
