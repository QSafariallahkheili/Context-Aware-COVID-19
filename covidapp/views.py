from django.shortcuts import render
from django.contrib.gis.utils import LayerMapping
from .models import Departments
from django.db.models import Sum
from django.core.serializers import serialize
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import Point
import re
from django.contrib.gis.measure import D, Distance


# Create your views here.
def indexPage(request):
    number = 22
    dep_name_column = Departments.objects.values_list('nom', flat=True) # it query one specific column with all the rows
    total_infect_column = Departments.objects.values_list('tot_infect', flat=True)
    total_infect= Departments.objects.aggregate(Sum('tot_infect'))

    name_array = []
    infected_array = []

    for x in dep_name_column:
        name_array.append(x)
    
    for x in total_infect_column:
        infected_array.append(x)
    
    #print(infected_array)

    # sending departments as Geojson file
    condition =  Departments.objects.all()
    departments = serialize('geojson', condition)
    # interactive querying and filtering departments by their names 
    if request.method=='POST' and 'depName' in request.POST:
        depName = request.POST.get('depName')
        condition = Departments.objects.filter(nom=depName)
        departments = serialize('geojson', condition)
    # interactive querying and filtering departments by the number of total infected people
    if request.method=='POST' and 'infectNo' in request.POST:
        infectNo = request.POST.get('infectNo')
        condition = Departments.objects.filter(tot_infect__gte=infectNo)
        departments = serialize('geojson', condition)
    if request.method=='POST' and 'deathNo' in request.POST:
        deathNo = request.POST.get('deathNo')
        condition = Departments.objects.filter(tot_death_field__gte=deathNo)
        departments = serialize('geojson', condition)
    
    dep_names_all = Departments.objects.values_list('nom', flat=True).order_by('nom')

    #Global variables to be filled and send to context
    lat = 47.101
    lon = 2.271
    zoom = 6
    user_dep_name = "a"
    userLat = 0
    userLon = 0
    neighbors = "hh"
    neighbor_array_name = []
    neighbor_dis = []
    neighbor_infection_rate = []
    #print(countryName)
    if request.method=='POST' and 'countryName' in request.POST:
        countryName = request.POST.get('countryName')
        lat = Departments.objects.values_list('lat', flat=True).get(nom=countryName)
        lon = Departments.objects.values_list('lon', flat=True).get(nom=countryName)
        zoom = 9
        #print(lat,lon)


    # getting user's context information  
    if request.method=='POST' and 'user_lat' in request.POST:
        user_lat = request.POST.get('user_lat')
        user_lon = request.POST.get('user_lon')
        userLat=float(user_lat.replace(',',''))
        userLon=float(user_lon.replace(',',''))
        user_location = Point(userLon, userLat, srid=4326)
        
        
        if Departments.objects.filter(geom__contains=user_location): # this checks if the user is inside the one of the polygons inside the Department layer
            user_dep_name = Departments.objects.values_list('nom', flat=True).get(geom__contains=user_location) #this queries the name of the department which user is at
            neighbors = Departments.objects.filter(geom__touches = Departments.objects.get(nom=user_dep_name).geom) # this query retrieve id of the departments which are the neighbor of "user_dep_name"
            neighbors_str = str(neighbors)
            neighbor_array = re.findall("(\d+)", neighbors_str)  # this line get the neighbors string and removes the unnecessary words in returned queryset
            #print(neighbor_array)
            #neighbor_array_name = []
            for i in neighbor_array: # getting the equivalent names for retrieved Ids
                neighbor_array_name.append(Departments.objects.values_list('nom', flat=True).get(id=i))
                neighbor_infection_rate.append(Departments.objects.values_list('tot_infect', flat=True).get(id=i)/(Departments.objects.values_list('population', flat=True).get(id=i)/1000)) # it computes the infection rate per 1000 population
            
            print(neighbor_infection_rate)
            print(neighbor_array_name)

            #neighbor_dis = []
            for i in neighbor_array_name:
                neighbor_dis.append(user_location.distance(Departments.objects.get(nom=i).geom)* 100) # computes the distance between two geometries
                
                
            #print(neighbor_dis)
            



        else:
            print("you are outside")

    context = {'total_infect':total_infect, 'name_array': name_array, 'infected_array': infected_array, 'departments': departments, 'lat':lat, 'lon':lon, 'zoom':zoom, 'user_dep_name':user_dep_name, 'userLon':userLon, 'userLat':userLat, 'neighbor_array_name': neighbor_array_name, 'neighbor_dis':neighbor_dis, 'dep_names_all':dep_names_all, 'neighbor_infection_rate': neighbor_infection_rate}
    return render(request, 'index.html', context)





