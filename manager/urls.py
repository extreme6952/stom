from django.urls import path
from . import views


app_name = 'content'

urlpatterns = [
    path('',views.ListHome.as_view(),name='home'),
    path('<int:year>/<int:month>/<int:day>/<slug:content>/',views.detail_services,name='detail_services')
]