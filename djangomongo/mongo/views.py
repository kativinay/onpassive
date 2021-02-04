import os
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import MongoForm
import base64
import pymongo
from django.core.files.storage import default_storage
from django.conf import settings
from bson.binary import Binary

# establish a connection to the database
connection = pymongo.MongoClient()

#get a handle to the mongo_db database
db = connection.mongo_db


# Create your views here.

class MongoView(View):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = MongoForm(request.POST, request.FILES)
        files = db.myfiles.find()
        lt = []
       
        context = {
            'form':form,
            'data':files
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = MongoForm()
        files = request.FILES['image']
        file_name = default_storage.save(files.name, files)
        file_path = settings.MEDIA_ROOT+"/"+file_name
        with open(file_path, "rb") as f:
            encoded = Binary(f.read())
            db.myfiles.insert({"image": file_name, "file": encoded, "description": "test" })
        mongo = MongoTestModel.objects.all().values()

        context = {
            'form':form,
            'data':mongo,
        }
        return render(request, self.template_name, context)


