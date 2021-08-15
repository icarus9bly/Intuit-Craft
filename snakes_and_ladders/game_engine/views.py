from django.shortcuts import render

# Create your views here.
def all_client_side(request):
    return render(request, "game_engine/canvas2.html")

def all_server_side(request):
    # Board Constraints:
    ladders={}
    lad_num=11
    for i in range(lad_num):
        ladders.update({'lad':})
    return render(request)