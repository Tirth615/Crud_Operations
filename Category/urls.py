from django.urls import path
from Category import views

urlpatterns = [

    path('',views.index),

    path('addcategory/',views.addcategory,name='addcategory/'),

    path('insertcategory/',views.insertcategory),

    path('viewcategory/',views.viewcategory,name='viewcategory/'),

    path('editcategory/',views.editcategory),

    path('deletecategory/',views.deletecategory),

    path("editcategory",views.editcategory),

    path("editcategory/updatecategory/",views.updatecategory),

]