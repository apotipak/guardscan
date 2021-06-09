from rest_framework import serializers 
from .models import Timescan
 
class TimeScanSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Timescan
        fields = ('id','site_code','date_scan','status','sh_code','sh_name','d_code','user_code','site_name','date_save','date_update','date_process','op1','op2','op3','op4','op5','upd_date','upd_by','upd_flag')

