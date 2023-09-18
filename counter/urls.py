from django.urls import path
from . import views
urlpatterns = [ 
    path('<int:form_id>/', views.count, name='count')
]