from django.urls import path
from .views import HadeethList, HadeethDetail
urlpatterns=[
    path('api/v1/', HadeethList.as_view(), name='list'),
    path('api/v1/<int:pk>/', HadeethDetail.as_view(), name='detail'),
    ]
