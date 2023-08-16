from django.shortcuts import render
from .models import ValueModel


def khojView(request):
	''' This django view take input values and search value from web page .check if search value 
	contains in input values .If contain display true and else it display false in the webpage .
	This function also save the user and sorted input values in the database .

	'''
	if request.method == 'POST':
		input_values= request.POST['input_values'] #get the input values from webpage
		search_value = request.POST['search_value'] ##get the input values from webpage
		user= request.user #get the user
		input_values_list = input_values.split(",") #convert the string into list

		#convert the elements of input_values_list from string into int and save them in a new list
		input_values_list_int = []
		for i in input_values_list:
			#if i != ',' and i != ' ':		
				input_values_list_int.append(int(i))	

		input_values_list_int.sort(reverse=True) #sort the list as desending order 
		list2str = ','.join(str(i) for i in input_values_list_int) #convert the sorted list into str

		#save input values and user in database
		value_object = ValueModel.objects.create(input_values=list2str,user=user) 
		value_object.save()
		result = int(search_value) in input_values_list_int #check if search value contains in input values

		context = {'result': result}
		return render(request, 'khoj.html', context)
	else:	
		return render(request, 'khoj.html')	
