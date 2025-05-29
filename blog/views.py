from django.shortcuts import render
from blog.models import Location
from blog.models import Food
from blog.models import Transport
import requests
import json


# Create your views here.


def show(request):
  
    countryTravelCost = []
    countryCurrencyCode = {}
    countryName={}
    countryActivity={}
    cCode =[]
    cList = []
    geonameid = []
    cityTravelCost = []
    cityName = []
    cityCurrencyCode = []
    cityActivityCost = []
    cityFood = []

    # getting information about country
    if 'query' in request.GET:
        # getting country code from url on pressing the search button
        countrycode = request.GET['query']
        countrycode = (countrycode[-2]+countrycode[-1])
        # Accessing the api for particular country code
        headers = {'X-API-KEY':'************************','Content-Type':'application/json'} #Enter API KEY
        url = 'https://www.budgetyourtrip.com/api/v3/costs/countryinfo/%s' % countrycode
        response = requests.get(url, headers=headers) # Saving the respose object from the api
        countryTravelCost = ((((response.json())['data']["costs"]))) # Country Travel Cost
        countryCurrencyCode = ((response.json())['data']["info"]["currency_code"]) # Country Currency Code
        countryName = ((response.json())['data']["info"]["name"]) # Country Name
        # for x in countryTravelCost:
        #     user1.append(x)

        # Accessing the api from country activity cost aganist particular country code
        headers = {'X-API-KEY':'****************************','Content-Type':'application/json'} #Enter API KEY
        url = 'https://www.budgetyourtrip.com/api/v3/costs/countryhighlights/%s' % countrycode
        response = requests.get(url, headers=headers) # Saving the respose object from the api
        countryActivity = ((response.json())['data']) # Country Activity Cost
        
       
       
    # getting information about city
    if 'sel1' in request.GET:
        # getting geonameid for city from url on pressing the search button
        geonameid = request.GET['sel1']
        headers = {'X-API-KEY':'***********************************','Content-Type':'application/json'} #Enter API KEY
        url = 'https://www.budgetyourtrip.com/api/v3/costs/locationinfo/%s' %geonameid
        response = requests.get(url, headers=headers) # Saving the respose object from the api
        cityTravelCost = ((((response.json())['data']["costs"]))) # city Travel Cost
        cityName = ((response.json())['data']["info"]["asciiname"]) # City Name
        cityCurrencyCode = ((response.json())['data']["info"]["currency_code"]) # City Currency Code
        
        
        headers = {'X-API-KEY':'************************************','Content-Type':'application/json'} #Enter API KEY
        url = 'https://www.budgetyourtrip.com/api/v3/activities/citysearch/%s' %cityName
        response = requests.get(url, headers=headers)
        cityActivityCost = ((response.json())['data']) # City Activity Costs
        
        headers = {'X-API-KEY':'**************************************','Content-Type':'application/json'} #Enter API KEY
        url = 'https://www.budgetyourtrip.com/api/v3/costs/highlights/%s' %geonameid
        response = requests.get(url, headers=headers)
        cityFood = ((response.json())['data']) # City Food
        
        
            
    # Accesing the api currency code for currency conversion
    headers = {'X-API-KEY':'**************************','Content-Type':'application/json'} #Enter API KEY
    response = requests.get('https://www.budgetyourtrip.com/api/v3/currencies', headers=headers)
    # test1 = response
    currencyCode = ((response.json())['data'])
    #test1 = test1['currency_code']
    #test1 == ((((response.json())['data']["currency_code"])))
    for x in currencyCode:
        cCode.append((x["currency_code"]))

    # Accessing the api for Country list populated in country search bar
    headers = {'X-API-KEY':'*******************************','Content-Type':'application/json'} #Enter API KEY
    response = requests.get('https://www.budgetyourtrip.com/api/v3/countries', headers=headers)
    # getting country list from the api
    countryList = response.json()
    countryList = countryList['data']
    #countryList = countryList[0]['name']
    for x in countryList:
        cList.append((x["name"]+" "+x["country_code"]))
        


    # passing data in variables to front end
    return render(request, 'blog/blog.html', {'cList':cList,
                                                   'countryTravelCost':countryTravelCost,
                                                   'countryCurrencyCode':countryCurrencyCode,
                                                   'countryName':countryName,
                                                   'countryActivity':countryActivity,
                                                   'cCode':cCode,
                                                   'cityTravelCost':cityTravelCost,
                                                   'cityName':cityName,
                                                   'cityCurrencyCode':cityCurrencyCode,
                                                   'cityActivityCost':cityActivityCost,
                                                   'cityFood':cityFood})



#def results(request):
 #   loc= Location.objects.values('location')
  #  foo= Food.objects.all()
   # trans= Transport.objects.values('transport')
    
    #content = {
    #'location':loc,
    #'food':foo,
    #'transport':trans,
    #}
    #return render(request, 'blog/results.html', content)

