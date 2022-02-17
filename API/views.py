from django.http import JsonResponse
from django.shortcuts import render
import urllib.request
import requests
import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import VideoDataSerializer
from .models import video_data
# from .models import unique_id
# # Create your views here.

# @api_view(['GET'])
# def get_video_data_by_id(request, unique_user_id):
#     user = unique_id.objects.get(user_id = unique_user_id)
#     all_user_videos = video_data.objects.filter(user_id = user)
#     serializer = VideoDataSerializer(all_user_videos, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_video_data(request, unique_user_id):
#     serializer = VideoDataSerializer(data=request.data)

#     if serializer.is_valid():
#         instance = serializer.save(commit=False)
#         instance.user_id= unique_id
#         instance.save
#     else:
#         print("Not a valid Data")
#     return Response(serializer.data)

    

@api_view(['GET'])
def Test(request, url):
    api_url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"
    querystring = {"url":url,"hd":"0"}
    headers = {
        'x-rapidapi-host': "tiktok-video-no-watermark2.p.rapidapi.com",
        'x-rapidapi-key': "7f9ace4cbdmshc72395aeeec405fp169c25jsn7ff5e0fe4baf"
        }

    response = requests.request("GET", api_url, headers=headers, params=querystring)
    print(response)

    #json.loads converts string dictionary to dictionary
    response_dict = json.loads(response.text)

    #The play_url below is the link to play the video without watermark
    video_data_dict = {
        'play_url': response_dict['data']['play'],
        'cover_photo_url': response_dict['data']['origin_cover'],
        'title': response_dict['data']['title']
    }
    print(video_data_dict['play_url'])

    #using the url lib we are able to save the video to our computer
    #urllib.request.urlretrieve(play_url, "video1.mp4")
    return Response(video_data_dict)


@api_view(['GET'])
def saved_videos(request):
    video_datas = video_data.objects.all()
    serializer = VideoDataSerializer(video_datas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def saved_video_detail(request, pk):
    video_datas = video_data.objects.get(id=pk)
    serializer = VideoDataSerializer(video_datas, many=False)
    return Response(serializer.data)
    

@api_view(['POST'])
def create_video_data(request):
    serializer = VideoDataSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        print("Not a valid Data")
    return Response(serializer.data)