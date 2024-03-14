from . import views
from django.urls import path
app_name = 'ecommerceapp'

urlpatterns = [
  path('', views.Allprocate, name="Allprocate"),
  path('<slug:c_slug>/', views.Allprocate, name="product_by_category"),
  path('<slug:c_slug>/<slug:pro_slug>/', views.proDetails, name="productDetails"),
]
