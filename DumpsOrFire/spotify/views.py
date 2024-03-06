from django.shortcuts import render
from . import generate_rating as gr
# from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'spotify/index.html')

def rate(request):
    context = {}
    context['search_type'] = 'track'
    # if request.method == 'GET':
    #     search_type = request.GET.get('search_type', 'track')
    #     if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
    #         return JsonResponse({'search_type': search_type})
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        search_type = request.POST.get('search_type', 'track')
        context['search_type'] = search_type
        if gr.get_track_popularity(user_input) is not None:
            context['rating'] = gr.get_track_popularity(user_input)
            context['image'] = gr.get_track_image(user_input)
        else:
            context['error'] = f"No result with name {user_input} found."

    return render(request, 'spotify/rate.html', context)
