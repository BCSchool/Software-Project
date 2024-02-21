from django.shortcuts import render
from . import generate_rating

# Create your views here.

def index(request):
    return render(request, 'spotify/index.html')

def home(request):
    rating = None
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        rating = generate_rating.get_track_popularity(user_input)
    return render(request, 'spotify/home.html', {'rating': rating})


        # try:
        #     context['rating'] = generate_rating(playlist_name)
        #     raise PlaylistNotFound("Playlist not found :(")
        # except PlaylistNotFound as e:
        #     context['error'] = str(e)

    # return render(request, 'spotify/home.html', context)
