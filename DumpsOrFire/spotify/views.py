from django.shortcuts import render
from . import generate_rating as gr

# from django.http import JsonResponse

from . import format_rating as fr

# Create your views here.

def index(request):
    return render(request, 'spotify/index.html')

def rate(request):
    context = {}
    if request.method == 'POST':
        '''Get user input and change search type text in search box'''
        user_input = request.POST.get('user_input')
        search_type = request.POST.get('search_type')

        # set default search type if none provided
        if not search_type:
            search_type = 'album'

        context['search_type'] = search_type

        if search_type == 'track':
            # track search
            if gr.get_track_popularity(user_input) is not None:
                '''get rating from api and description from json file'''
                context['rating'] = gr.get_track_popularity(user_input)

                desc, img = fr.format_rating(gr.get_track_popularity(user_input))

                context['description'] =  desc
                context['reaction'] = f"static/spotify/rating_reaction/{img}"

                context['image'] = gr.get_track_image(user_input)
                context['name'] = gr.get_track_name(user_input)
            else:
                context['error'] = f"No result with name {user_input} found."

        elif search_type == 'album':
            # album search
            if gr.get_album_popularity(user_input) is not None:
                context['rating'] = gr.get_album_popularity(user_input)

                desc, img = fr.format_rating(gr.get_track_popularity(user_input))

                context['description'] =  desc
                context['reaction'] = f"static/spotify/rating_reaction/{img}"

                context['image'] = gr.get_album_image(user_input)
                context['name'] = gr.get_album_name(user_input)

    return render(request, 'spotify/rate.html', context)
