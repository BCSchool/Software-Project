from django.shortcuts import render
from . import generate_rating as gr

# from django.http import JsonResponse

from . import format_rating as fr

# Create your views here.

def index(request):
    return render(request, 'spotify/index.html')

def rate(request):
    context = {}
    context['search_type'] = 'track'
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        search_type = request.POST.get('search_type', 'album')
        context['search_type'] = search_type
        if gr.get_track_popularity(user_input) is not None:
            if search_type == 'track':
                context['rating'] = gr.get_track_popularity(user_input)
                context['description'] =  fr.format_rating(gr.get_track_popularity(user_input))
                # context['rating_reaction'] =  fr.get_rating_reaction(letter_rating='A')
                context['image'] = gr.get_track_image(user_input)

            elif search_type == 'album':
                context['rating'] = gr.get_album_popularity(user_input)
                context['description'] = "yo"
        else:
            context['error'] = f"No result with name {user_input} found."

    return render(request, 'spotify/rate.html', context)
