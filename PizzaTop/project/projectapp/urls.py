from django.conf.urls import url
from projectapp import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[

url(r'^toppingurl',views.ToppingView.as_view(),name='ToppingView'),
]
