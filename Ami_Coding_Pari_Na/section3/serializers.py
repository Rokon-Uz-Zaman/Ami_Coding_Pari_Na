
from rest_framework import serializers 
from section2.models import ValueModel

class ValueModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = ValueModel
		fields = ['input_values','timestamp']
