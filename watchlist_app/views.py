# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse
#
# # Create your views here.
# # this is  function based view
# def movie_list(request):
#     movies = Movie.objects.all()
#     print(movies.values())
#     data = {'movies': list(movies.values())}
#
#     return JsonResponse(data)
#
# def movie_details(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         'id': movie.id,
#         'name': movie.name,
#         'description': movie.description,
#         'is_active': movie.is_active
#     }
#     print(movie.name)
#     return JsonResponse(data)