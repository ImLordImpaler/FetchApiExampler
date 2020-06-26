
from django.urls import path, include 
from . import views
urlpatterns = [
 path('' , views.index , name = 'home') ,
  path('product/<str:pk>' , views.productDetail , name = 'product'), 
  path('updateItem' , views.updateItem , name = 'updateItem')

]
