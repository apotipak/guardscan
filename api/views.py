from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import django.db as db
from django.db import connection
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .serializers import TimeScanSerializer
from .models import Timescan
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status


@api_view(['GET', 'POST'])
def timescan_list_v1(request):
    if request.method == 'GET':
        print("DEBUG : GET")
        timescan = Timescan.objects.all()
        
        site_code = request.query_params.get('site_code', None)
        if site_code is not None:
            timescan = timescan.filter(site_code__icontains=site_code)
        
        timescan_serializer = TimeScanSerializer(timescan, many=True)
        return JsonResponse(timescan_serializer.data, safe=False)
 
    elif request.method == 'POST':
        print("DEBUG : POST")
        serializer = TimeScanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
 

@api_view(['GET'])
def timescan_detail_v1(request, pk):
    try: 
        timescan = Timescan.objects.get(pk=pk) 
    except Timescan.DoesNotExist: 
        return JsonResponse({'message': 'Timescan does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET':         
        timescan_serializer = TimeScanSerializer(timescan)
        return JsonResponse(timescan_serializer.data) 
     

# @csrf_exempt
'''
@api_view(['GET', 'POST'])
def timescan_list(request):
    if request.method == 'GET':
        timescan_obj = None
        timescan_list = []
        record = {}
        error_message = ""

        sql = "select * from timescan;"

        try:
            cursor = connection.cursor()
            cursor.execute(sql)
            timescan_obj = cursor.fetchall()
            
        except db.OperationalError as e:        
            error_message = "<b>Error: please send this error to IT team</b><br>" + str(e)
        except db.Error as e:
            error_message = "<b>Error: please send this error to IT team</b><br>" + str(e)
        finally:
            cursor.close()

        if timescan_obj is not None:
            message = "Success"
            for item in timescan_obj:
                emp_id = item[7]                
                site_code = item[0]
                status = item[3]
                date_scan = item[1]


                record = {
                    "emp_id": emp_id,
                    "site_code": site_code,
                    "status": status,
                    "date_scan": date_scan,
                }

                timescan_list.append(record)
        else:
            error_message = "Error"        

        content = {'results': timescan_list}

        return Response(content)

    elif request.method == 'POST':
        
        site_code = request.POST.get('site_code')
        date_scan = request.POST.get('date_scan')
        status = request.POST.get('status')
        sh_code = request.POST.get('sh_code')
        sh_name = request.POST.get('sh_name')
        d_code = request.POST.get('d_code')        
        user_code = request.POST.get('user_code')
        site_name = request.POST.get('site_name')
        date_save = request.POST.get('date_save')
        date_update = request.POST.get('date_update')
        date_process = request.POST.get('date_process')
        op1 = request.POST.get('op1')
        op2 = request.POST.get('op2')
        op3 = request.POST.get('op3')
        op4 = request.POST.get('op4')
        op5 = request.POST.get('op5')
        upd_date = request.POST.get('upd_date')
        upd_by = request.POST.get('upd_by')
        upd_flag = request.POST.get('upd_flag')
        
        timescan = Timescan(
            site_code = site_code,
            date_scan = date_scan,
            status = status,
            sh_code = sh_code,
            user_code = user_code,
        )
        timescan.save()
        
        content = {'message': "Success"}
        return Response(content)
'''
