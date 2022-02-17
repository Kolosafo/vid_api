from django.urls import path
from . import views

urlpatterns =[
    path('test/<path:url>', views.Test, name='test'),
    path('saved_videos/', views.saved_videos, name='saved_videos'),
    path('create_video_data/', views.create_video_data, name='create_video_data'),
    path('saved_video_detail/<str:pk>', views.saved_video_detail, name='saved_video_detail'),
    # path('get_by_id/<str:unique_user_id>', views.get_video_data_by_id, name='get_video_data_by_id'),

]