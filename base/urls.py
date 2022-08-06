
from django.urls import path
from base import views

urlpatterns = [
    path('',views.Home, name="home"),
    path('create',views.Create,name = "create"),
    path('listview',views.List_View,name = "listview"),
    path('detailview/<int:id>', views.Detail_View,name = "detailview"),
    path('updateview/<int:id>', views.Update_View,name = "updateview"),
    path('deleteview/<int:id>', views.Delete_View,name = "deleteview"),
]