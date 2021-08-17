from django.shortcuts import render, HttpResponse
from game_engine.loggers import mana_logger
# Create your views here.
def no_js(request):
    mana_logger.info('No js view is being used')
    return render(request, "game_engine/no_js.html")

def basic_grid(request):
    mana_logger.info('Basic grid is being used')
    return render(request, "game_engine/basic_grid.html")    

def all_server_side(request):
    # Board constraints
    # Head > tail
    # Head and tail should be in range(2,99)
    board_details={
    'snakes':[
        {
            'snake1':{'head':'val','tail':'val'}
        },
        {
            'snake2':{'head':'val','tail':'val'}
        }
    ],
    'ladders':[
        {
            'ladder1':{'head':'val','tail':'val'}
        },
        {
            'ladder2':{'head':'val','tail':'val'}
        }
    ]
    }
    return HttpResponse("Holla")

def test(request):
    mana_logger.debug('Exception occurred:')
    return render(request, 'game_engine/game_canvas.html')