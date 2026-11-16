from django.urls import path, include
from watchlist_app.api.views import WatchListAV, WatchListDetailsAV, StreamPlatformAV, StreamPlatformDetailsAV, \
    ReviewAV, ReviewDetailsAV, ReviewCreateAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchListDetailsAV.as_view(), name='movie-details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-platform'),
    path('stream/<int:pk>', StreamPlatformDetailsAV.as_view(), name='stream-platform-details'),
    path('stream/<int:pk>/review-create/', ReviewCreateAV.as_view(), name='create-review'),
    path('stream/<int:pk>/reviews/', ReviewAV.as_view(), name='review-list'),
    path('stream/reviews/<int:pk>', ReviewDetailsAV.as_view(), name='review-details'),
]
