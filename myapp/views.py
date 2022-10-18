from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

def shorten_url(request):
	context = {
		"submitted": False,
		"error": False
	}

	if request.method == 'POST':
		user_data = request.POST 				# dict
		long_url = user_data['longurl']
		custom_name = user_data['custom_name']

		try:
			# CREATE
			obj = URL_table(long_url = long_url, custom_name = custom_name)
			obj.save()

			# READ
			data = {
				"longurl": obj.long_url,
				"shorturl": obj.custom_name,
				"date": obj.created_date,
				"clicks": obj.visit_count
			}

			context["submitted"] = True
			context["data"] = data

		except Exception as e:
			print(e)
			context["error"] = True

	return render(request, "index.html", context)


def redirect_url(request, custom_name):
	try:
		row = URL_table.objects.get(custom_name = custom_name)
		long_url = row.long_url
		row.visit_count += 1
		row.save()
		return redirect(long_url)

	except Exception as e:
		print(e)
		return HttpResponse("This custom name has no mapping")


def all_analytics(request):
	rows = URL_table.objects.all()

	context = {
		"rows": rows
	}

	return render(request, "all-analytics.html", context)


def hello_world(request):
	return HttpResponse("Hello world!")


def task(request):
	context = {
		"my_name": "John",
		"x": 15
	}

	return render(request, "test.html", context)