# from django.db import models
from djongo import models
# from django_mongodb_engine.storage import GridFSStorage
# from gridfs import GridFS
# from bson import objectid
from django.conf import settings
from djongo.storage import GridFSStorage
grid_fs_storage = GridFSStorage(collection='myfiles', base_url=''.join([settings.BASE_URL, 'myfiles/']))


class MongoTestModel(models.Model):
    image = models.ImageField(upload_to='myfiles', storage=grid_fs_storage)
   
    class Meta:
        db_table = 'myfiles'
    
    def __str__(self):
        return self.name