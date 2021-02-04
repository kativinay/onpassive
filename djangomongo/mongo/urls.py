from django.urls import path
from mongo.views import MongoView

urlpatterns = [
    path('', MongoView.as_view(), name='mongo_view'),
]