from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.views import generic
from django.db import connection
import pandas as pd

from .models import Flux, Flux2

# Create your views here.
def index(request):
	query = request.GET.get('q')
	data = Flux.objects.raw("SELECT * FROM queries_flux WHERE flux_name = '{}'".format(query))
	data2 = Flux2.objects.raw(f"SELECT * FROM queries_flux2 WHERE description LIKE '%%{query}%%'")

	cursor = connection.cursor()
	cursor.execute("""SELECT * FROM queries_flux LIMIT 5""")
	# sample JOIN query
	# cursor.execute("""SELECT * FROM queries_flux
	# 	INNER JOIN queries_flux2 on queries_flux.flux_name = queries_flux2.flux_name
	# 	LIMIT 5""")
	rows = cursor.fetchall()

	columns = [col[0] for col in cursor.description]

	col_indices = [i for i, value in enumerate(columns)]

	helper_dict = list(range(18))

	for p in data:
		print(p)

	car_names = request.GET.get('cars')
	print(car_names)

	context = {
		"request_data": data,
		"request_data2": data2,
		"rows": rows,
		"columns": columns,
		"col_indices": col_indices,
		"helper_dict": helper_dict,
	}
	return render(request, "queries/requests.html", context)

def detail(request, flux_id):
	# only attributes from the first dataset are fetched here
	query = get_object_or_404(Flux, pk=flux_id)
	attrs = list(query.__dict__.keys())[1:]
	context = {
		"query": query,
		"attrs": attrs,
	}
	return render(request, 'queries/detail.html', context)

def detail2(request, flux_id):
	# only attributes from the second dataset are fetched here
	query2 = get_object_or_404(Flux2, pk=flux_id)
	context = {
		"query2": query2,
	}
	return render(request, 'queries/detail2.html', context)


def home(request):
	context = {}
	return render(request, 'queries/home.html', context)













