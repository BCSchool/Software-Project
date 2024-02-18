from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'spotify/index.html')

def home(request):
    rating = None
    if request.method == 'POST':
        playlist_name = request.POST.get('playlist_name')
        rating = 7
        # try:
        #     context['rating'] = generate_rating(playlist_name)
        #     raise PlaylistNotFound("Playlist not found :(")
        # except PlaylistNotFound as e:
        #     context['error'] = str(e)

    # return render(request, 'spotify/home.html', context)
    return render(request, 'spotify/home.html', {'rating': rating})
