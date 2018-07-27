from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urlencode

sunday={'sday':'1532185200','sdate':'0'}
monday={'sday':'1532271600','sdate':'1'}
tuesday ={'sday':'1532358000','sdate':'2'}
wednesday={'sday':'1532444400','sdate':'3'}
thursday={'sday':'1532530800','sdate':'4'}
friday={'sday':'1532617200','sdate':'5'}
saturday={'sday':'1532703600','sdate':'6'}


def keyboard(request):
    return JsonResponse({
        'type':'buttons',
        'buttons':['일','월','화','수','목','금','토']
    })

@csrf_exempt
def message(request):
    json_str = ((request.body)).decode('utf-8')
    received_json_data = json.loads(json_str)

    user=received_json_data['user_key']
    type=received_json_data['type']
    choice=received_json_data['content']

    if choice=='일':
        return JsonResponse({
            'message':{
                'text':'str'
            },
            'keyboard':{
                'type':'buttons',
                'buttons':['일','월','화','수','목','금','토']
            }
        })
    elif choice=='월':
        return JsonResponse({
            'message':{
                'text':'str'
            },
            'keyboard':{
                'type':'buttons',
                'buttons':['일','월','화','수','목','금','토']
            }
        })
    elif choice=='화':
        return JsonResponse({
            'message':{
                'text':'str'
            },
            'keyboard':{
                'type':'buttons',
                'buttons':['일','월','화','수','목','금','토']
            }
        })
    elif choice=='수':
        return JsonResponse({
            'message':{
                'text':'str'
            },
            'keyboard':{
                'type':'buttons',
                'buttons':['일','월','화','수','목','금','토']
            }
        })
    elif choice=='목':
        return JsonResponse({
            'message':{
                'text':'str'
            },
            'keyboard':{
                'type':'buttons',
                'buttons':['일','월','화','수','목','금','토']
            }
        })
    elif choice=='금':
        return JsonResponse({
            'message':{
                'text':'str'
            },
            'keyboard':{
                'type':'buttons',
                'buttons':['일','월','화','수','목','금','토']
            }
        })
    else:
        return JsonResponse({
            'message':{
                'text':"토요일 입니다!"
            },
            'keyboard':{
                'type':'buttons',
                'buttons':['일','월','화','수','목','금','토']
            }
        })
