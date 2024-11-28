from django.contrib import admin
from django.urls import path
from . import views

app_name = 'collection'

urlpatterns = [
    path('',views.MasterView.as_view(),name='master'),
    path('post/',views.CreateImgView.as_view(),name='post'),
    path('post_done/',views.PostSuccessView.as_view(),name='post_done'),
    path('collection/<int:category>',views.CategoryView.as_view(),name='collection_cat'),
    path('user_names/<int:user>',views.UserNameView.as_view(),name='user_names'),
    path('collect_detail/<int:pk>',views.CollectDetailView.as_view(),name = 'collect_detail'),
    path('mypage/',views.MypageView.as_view(),name = 'mypage'),
    path('collect_delete/<int:pk>',views.CollectDeleteView.as_view(),name = 'collect_delete'),
    path('contact/',views.ContactView.as_view(),name='contact')
]
