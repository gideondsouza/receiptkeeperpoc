import urllib
import logging

from google.appengine.api import users
from google.appengine.ext import ndb

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

import jinja2
import webapp2

import sys
import os

import pdb
import datetime

from base import base_handlers
from models import receipt

class Add(base_handlers.BaseHandler, blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        upload_files = self.get_uploads('scan')
        blob_info = upload_files[0]
        #pdb.set_trace()
        r = receipt.Receipt()
        r.total = int(self.request.POST.get('total'))
        r.tax = int(self.request.POST.get('tax'))
        r.merchant = self.request.POST.get('merchant')
        r.date = datetime.datetime.now()#self.request.POST.get('date')
        r.category = self.request.POST.get('category')
        r.note = self.request.POST.get('note')
        r.scankey = str(blob_info.key())
        r.put()
        upload_url = blobstore.create_upload_url('/upload')
        self.render_template("add.html", {"upload_url": upload_url})

# store blob_info.key() into the ReceiptModel)
    def get(self):
        upload_url = blobstore.create_upload_url('/upload')
        self.render_template("add.html", {"upload_url": upload_url})


class View(base_handlers.BaseHandler):
    def get(self, id):
        pass
        # return page to view A single receipt

class Scan(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, resx):
        resx = str(urllib.unquote(resx))
        blob_info = blobstore.BlobInfo.get(resx)
        self.send_blob(blob_info)

