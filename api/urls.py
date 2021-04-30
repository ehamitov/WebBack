from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from api.views_fbv import *
from api.views_cbv import *

urlpatterns = [
    path('login/' , obtain_jwt_token),
    path('categories/' , category_list ),
    path('categories/<int:category_id>' , category_detail),
    path('categories/<int:category_id>/books/', category_products ),
    path('products/' , ProductListAPIView.as_view()),
    path('products/<int:product_id>/' , ProductDetailAPIView.as_view()),
    path('productss/cheap_three/' ,  ThreeCheapProductAPIView.as_view())
]