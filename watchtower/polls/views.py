import requests
import time
import alpha_vantage
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def security_search(request):
	#requiered field
	identifiers = request.GET.get('ids', '')

	start_date = request.GET.get('start', str(int(time.strftime('%Y%m%d')) - 50000))
	end_date = request.GET.get('end', time.strftime('%Y%m%d'))

	security_search_results = requests.get("https://www.blackrock.com/tools/hackathon/search-securities", params = {
		'identifiers': identifiers, 
		'startDate': start_date, 
		'toDate': end_date
		})
	
	return HttpResponse(security_search_results.json)

def performance_data(request):
	#requiered field
	identifiers = request.GET.get('ids', '')

	historic_returns = bool(request.GET.get('hisret', False))
	returnsType = request.GET.get('returnsType', 'MONTHLY')
	start_date = request.GET.get('start', str(int(time.strftime('%Y%m%d')) - 50000))
	end_date = request.GET.get('end', time.strftime('%Y%m%d'))

	performance_data_results = requests.get("https://www.blackrock.com/tools/hackathon/performance", params = {
		'identifiers': identifiers,
		'includePositionReturns': historic_returns,
		'returnsType': returnsType,
		'startDate': start_date,
		'endDate': end_date
		})

	return HttpResponse(performance_data_results.json)