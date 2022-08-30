from django.shortcuts import render
import requests
import json
from .models import m_usernames,m_userdetails
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.core import serializers

# Create your views here.

from django.http import HttpResponse

pagerecords = 10

def index(request):
	return HttpResponse(" Welcome !")

def get_filtered_data_api(request):
	vUsername = request.GET.get('username', '')
	vFirstName = request.GET.get('first_name', '')
	vLastName = request.GET.get('last_name', '')
	vGender = request.GET.get('gender', '')
	if vGender=='male' or vGender == 'female':
		user_list = m_usernames.objects.filter(gender=vGender, first_name__contains=vFirstName , last_name__contains=vLastName, username__contains=vUsername)[0:100]
	else:
		user_list = m_usernames.objects.filter(first_name__contains=vFirstName , last_name__contains=vLastName, username__contains=vUsername)[0:100]
	qs_json = serializers.serialize('json', user_list)
	return HttpResponse(qs_json, content_type='application/json')



def all_user_list_screen(request):
	global pagerecords
	user_list = m_usernames.objects.all()
	page = request.GET.get('page', 1)
	
	if request.GET.get('pagerecords') == "5":
		pagerecords = 5
	elif request.GET.get('pagerecords') == "10":
		pagerecords = 10
	elif request.GET.get('pagerecords') == "20":
		pagerecords = 20
	elif request.GET.get('pagerecords') == "50":
		pagerecords = 50
	elif request.GET.get('pagerecords') == "100":
		pagerecords = 100
	elif request.GET.get('pagerecords') == "500":
		pagerecords = 500
	elif request.GET.get('pagerecords') == "1000":
		pagerecords = 1000

	print("pagerecords "+str(pagerecords))

	paginator = Paginator(user_list, pagerecords)
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
 		users = paginator.page(1)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)

	return render(request, 'user_list.html', { 'users': users,'pagerecords':pagerecords, 'total_users':paginator.count})


def fetch_random_data_screen(request):
	user_list = m_usernames.objects.all()
	toastMsg = ""
	if 'toast' in request.session:
		toastMsg = request.session['toast']
	request.session['toast'] = ''
	return render(request, 'fetch_data.html', {'current_records':len(user_list),'toastMsg':toastMsg})

def clear_database_api(request):
	user_list = m_usernames.objects.all()
	user_list.delete()
	request.session['toast'] = "All records deleted successfully!"
	return redirect('fetch_random_data_screen')



def fetch_random_data_api(request):
	vMsg = ""
	inputUserCount = str(1)
	toastMsg = "test"
	request.session['toast'] = ''
	if request.method == 'POST':
		inputUserCount=str(request.POST.get('inputUserCount'))
		if int(inputUserCount)>5000:
			inputUserCount = str(5000)
	try:
		response = requests.get('https://randomuser.me/api/?results='+inputUserCount).json()  # Getting data from randomuser.me
		for record in response['results']:
			vFirst_name = record['name']['first']
			vLast_name = record['name']['last']
			vUsername = record['login']['username']
			vEmail = record['email']
			gender = record['gender']
			id_type = record['id']['name']
			id_value = record['id']['value']
			location_city = record['location']['city']
			location_state = record['location']['state']
			loation_country = record['location']['country']
			location_postcode = record['location']['postcode']
			dob = record['dob']['date']
			registered_date = record['registered']['date']
			phone = record['phone']
			cell = record['cell']
			picture = record['picture']['large']
			nat = record['nat']
			user = m_usernames(username = vUsername,first_name=vFirst_name,last_name=vLast_name,gender=gender,id_type = id_type,id_value=id_value)
			details = m_userdetails(email= vEmail,username = user, location_city=location_city,location_state=location_state,loation_country=loation_country,location_postcode=location_postcode,dob=dob,registered_date=registered_date,phone=phone,cell=cell,picture=picture,nat=nat)
			user.save()
			details.save()
			vMsg = str(len(response['results']))+" Users fetched and saved successfully!"
	except:
		vMsg = "Error in randomuser.me api data"


	request.session['toast'] = vMsg

	return redirect('fetch_random_data_screen')
	
def search_users_screen(request):
	user_list = m_usernames.objects.all()[:10]
	return render(request, 'search_users_screen.html', {'user_list' : user_list})



