from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from diary.models import Diary
from diary.models_data import DbUploader
from diary.serializers import DiarySerializer


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def process(request):
    return JsonResponse({'process': 'SUCCESS'})


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def find(request, user_id, year, month, day):
    print("********** find START **********")
    print(f'date : {year}-{month}-{day}')
    diary = Diary.objects.filter(user_id=int(user_id), diary_date__year= year, diary_date__month=month, diary_date__day=day).values()[0]
    print(diary)
    serializer = DiarySerializer(diary).data
    print("********** serializer **********")
    print(serializer)
    return JsonResponse(data=serializer, safe=False)


@api_view(['PUT'])
@parser_classes([JSONParser])
def modify(request):
    print("********** modify START **********")
    edit = request.data
    # print(edit)
    diary = Diary.objects.get(pk=edit['id'])
    db = Diary.objects.filter(pk=edit['id']).values()[0]
    # print(diary)
    db['memo'] = edit['memo']
    db['diary_date'] = edit['diary_date']
    db['log_id'] = edit['log_id']
    serializer = DiarySerializer(data=db)
    if serializer.is_valid():
        serializer.update(diary, db)
        return JsonResponse(data=serializer.data, safe=False)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def upload(request):
    print("********** NEW diary upload START **********")
    DbUploader().insert_data()
    return JsonResponse({'NEW diary': 'SUCCESS'})

