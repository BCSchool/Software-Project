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
        search_type = request.POST.get('search_type', 'track')
        context['search_type'] = search_type
        if gr.get_track_popularity(user_input) is not None:
            context['rating'] = gr.get_track_popularity(user_input)
            desc, img = fr.format_rating(gr.get_track_popularity(user_input))
            context['description'] =  desc
            context['reaction'] = f"static/spotify/rating_reaction/{img}"
            context['image'] = gr.get_track_image(user_input)
            context['name'] = gr.get_track_name(user_input)
        else:
            context['error'] = f"No result with name {user_input} found."

    return render(request, 'spotify/rate.html', context)
