from django.urls import path, re_path
from . import views

urlpatterns =[
    path('test/<path:url>', views.Test, name='test'),
    path('saved_videos/', views.saved_videos, name='saved_videos'),
    path('create_video_data/<str:DEVICE_ID>', views.create_video_data, name='create_video_data'),
    path('saved_video_detail/<str:pk>', views.saved_video_detail, name='saved_video_detail'),
    path('get_by_id/<str:unique_user_id>', views.get_video_data_by_id, name='get_video_data_by_id'),

    #THE URL BELOW WHEN CALLED ALONGSIDE THE PARAMETERS WILL SAVE A DOWNLOADED VIDEO TO THE BACKEND
    path('save/<str:DEVICE_ID>/<path:video_url>/', views.save_to_downloads, name='save_to_downloads'),


]