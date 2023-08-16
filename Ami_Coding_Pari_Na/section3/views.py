from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from section2.models import ValueModel
from .serializers import ValueModelSerializer


@api_view(["GET"])
def valueApiView(request,start_datetime,end_datetime,user_id):
	''' This view function take start_datetime , end_datetime , user_id as parameter .
	    return  all input values the user ever entered within 
	    start_datetime (inclusive) and end_datetime ( inclusive).
	'''
	start_datetime=str(start_datetime) #convert start_datetime into string 
	end_datetime=str(end_datetime) #convert end_datetime into string
	#Get all input values the user ever entered within start_datetime (inclusive) and end_datetime ( inclusive).
	value_obj= ValueModel.objects.filter(timestamp__range = [ start_datetime,end_datetime],user_id=user_id)
	value_seri= ValueModelSerializer(value_obj,many=True) #serialize 
	
	payload = value_seri.data
	#modify datetime format
	for i in payload:
		i['timestamp']=i['timestamp'].replace("T"," ")

	data = {"status": "succes","user_id":user_id,"payload": payload}
	return Response(data)	


