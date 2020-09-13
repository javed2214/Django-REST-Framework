
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from hrm.api import UserList, UserDetail, UserAuthentication

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^api/users_list/$', UserList.as_view(), name = 'user_list')
    path('', views.index, name = 'index'),
    path('viewdata/', views.viewdata, name = 'view_data'),
    path('api/users_list/', UserList.as_view(), name = 'user_list'),
    url(r'^api/users_list/(?P<employee_id>\d+)/$', UserDetail.as_view(), name = 'user_detail'),
    url(r'^api/auth/$', UserAuthentication.as_view(), name = 'user_authentication')
]
