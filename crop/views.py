from django.shortcuts import render, redirect
from django.http import HttpResponse
from crop.test import cropping
from .models import *
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView
from django.core.files.storage import FileSystemStorage
# Create your views here.
import cv2
import os
import numpy
from time import sleep

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View

from .forms import PhotoForm
from .models import Photo

from zipfile import ZipFile

class Home(TemplateView):
	template_name = 'index.html'

def home(request):
	return render(request, 'crop/index.html')

def success(request):
	return render(request, 'crop/success.html')
def about(request):
	return render(request, 'crop/about.html', {'title': 'about'})

def photoform(request, *args, **kwargs):
	if request.method == "POST":
		form = PhotoForm(request.POST, request.FILES)
		if form.is_valid():
			a = form.save()
			imge = list(Photo.objects.filter(post__id = a.id))
			index = 0
			query_str = ""
			image_number = 0
			image_files = []
			for img in imge:
				image = cv2.imread(img.image.path)
				original = image.copy()
				gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
				blurred = cv2.GaussianBlur(gray, (3, 3), 0)
				thresh = cv2.threshold(blurred, 230,255,cv2.THRESH_BINARY_INV)[1]
				# Find contours
				cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
				cnts = cnts[0] if len(cnts) == 2 else cnts[1]
				# Iterate thorugh contours and filter for ROI

				for c in cnts:
					x,y,w,h = cv2.boundingRect(c)
					cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
					ROI = original[y:y+h, x:x+w]
					if w>120 or h>120:
						old_dir = os.getcwd()
						#os.chdir(old_dir + "/photoscan/mysite/crop/static/crop/images")
						os.chdir(old_dir + "/crop/static/crop/images")
						cv2.imwrite("ROI_" + str(img.uuid) + "_{}.jpeg".format(image_number), ROI)
						os.chdir(old_dir)
						image_files += ["ROI_" + str(img.uuid) + "_" + str(image_number) + ".jpeg"]
						image_number += 1
				index += 1


				#cv2.imshow('thresh', thresh)
				#cv2.imshow('image', image)
				cv2.waitKey(0)

			old_dir = os.getcwd()
			#os.chdir(old_dir + "/photoscan/mysite/crop/static/crop/images")
			os.chdir(old_dir + "/crop/static/crop/images")
			# writing files to a zipfile
			with ZipFile("photos_" + str(a.uuid) + ".zip", "w") as zip:
				# writing each file one by one
				for file in image_files:
					print(file)
					zip.write(file)
			query_str = "file=photos_" + str(a.uuid)
			os.chdir(old_dir)
			return redirect('/success?' + query_str)

		else:
			form = PhotoForm()
	else:
		form = PhotoForm()
	return render(request, 'crop/start.html', {'form': form})
