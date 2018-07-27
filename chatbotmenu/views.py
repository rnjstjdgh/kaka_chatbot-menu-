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
        url_site = 'https://dgucoop.dongguk.edu/store/store.php?w=4&l=1'  # 기본 사이트 url형식
        data = urlencode(sunday).encode('utf-8')  # urlencode부분에 원하는 요일이 들어가면 됨
        html = Request(url_site, data)
        webpage = urlopen(html).read()
        soup = BeautifulSoup(webpage, "html.parser")  # url에 쿼리를 보내서 내가 원하는 날짜에 해당하는 정보를 크롤링하기!
        # print(soup)

        root = soup.find('td', align='center')
        list_menu_table = root.find_all('table', cellspacing='1')
        list_loc_table = root.find_all('td', class_='menu_st')
        dic = {}
        for i in range(7):
            # print(list_loc_table[i].text.strip())
            lunch = list_menu_table[i].find_all('tr')
            if i == 6:
                # print(lunch[5].text)
                dic[list_loc_table[i].text] = lunch[5].text.split()
            else:
                # print(lunch[1].text)
                dic[list_loc_table[i].text] = lunch[1].text.split()

            # print(list_menu_table[i].text.strip())
        #print(dic)
        #print('=' * 200)
        str = ''
        for i in dic.items():
            # print(i)
            str += i[0] + '-->' + '\n'
            for j in i[1]:
                str += j + '/'
            str += '\n'
        #print(str)
        return JsonResponse({
            'message':{
                'text':str
            },
            'keyboard':{
                'type':'buttons',
                'buttons':['일','월','화','수','목','금','토']
            }
        })
    elif choice=='월':
        url_site = 'https://dgucoop.dongguk.edu/store/store.php?w=4&l=1'  # 기본 사이트 url형식
        data = urlencode(monday).encode('utf-8')  # urlencode부분에 원하는 요일이 들어가면 됨
        html = Request(url_site, data)
        webpage = urlopen(html).read()
        soup = BeautifulSoup(webpage, "html.parser")  # url에 쿼리를 보내서 내가 원하는 날짜에 해당하는 정보를 크롤링하기!
        # print(soup)

        root = soup.find('td', align='center')
        list_menu_table = root.find_all('table', cellspacing='1')
        list_loc_table = root.find_all('td', class_='menu_st')
        dic = {}
        for i in range(7):
            # print(list_loc_table[i].text.strip())
            lunch = list_menu_table[i].find_all('tr')
            if i == 6:
                # print(lunch[5].text)
                dic[list_loc_table[i].text] = lunch[5].text.split()
            else:
                # print(lunch[1].text)
                dic[list_loc_table[i].text] = lunch[1].text.split()

            # print(list_menu_table[i].text.strip())
        #print(dic)
        #print('=' * 200)
        str = ''
        for i in dic.items():
            # print(i)
            str += i[0] + '-->' + '\n'
            for j in i[1]:
                str += j + '/'
            str += '\n'
        #print(str)

        return JsonResponse({
            'message':{
                'text':str
            },
            'keyboard':{
                'type':'buttons',
                'buttons':['일','월','화','수','목','금','토']
            }
        })
    elif choice=='화':
        url_site = 'https://dgucoop.dongguk.edu/store/store.php?w=4&l=1'  # 기본 사이트 url형식
        data = urlencode(tuesday).encode('utf-8')  # urlencode부분에 원하는 요일이 들어가면 됨
        html = Request(url_site, data)
        webpage = urlopen(html).read()
        soup = BeautifulSoup(webpage, "html.parser")  # url에 쿼리를 보내서 내가 원하는 날짜에 해당하는 정보를 크롤링하기!
        # print(soup)

        root = soup.find('td', align='center')
        list_menu_table = root.find_all('table', cellspacing='1')
        list_loc_table = root.find_all('td', class_='menu_st')
        dic = {}
        for i in range(7):
            # print(list_loc_table[i].text.strip())
            lunch = list_menu_table[i].find_all('tr')
            if i == 6:
                # print(lunch[5].text)
                dic[list_loc_table[i].text] = lunch[5].text.split()
            else:
                # print(lunch[1].text)
                dic[list_loc_table[i].text] = lunch[1].text.split()

            # print(list_menu_table[i].text.strip())
        #print(dic)
        #print('=' * 200)
        str = ''
        for i in dic.items():
            # print(i)
            str += i[0] + '-->' + '\n'
            for j in i[1]:
                str += j + '/'
            str += '\n'
        #print(str)

        return JsonResponse({
            'message':{
                'text':str
            },
            'keyboard':{
                'type':'buttons',
                'buttons':['일','월','화','수','목','금','토']
            }
        })
    elif choice=='수':
        url_site = 'https://dgucoop.dongguk.edu/store/store.php?w=4&l=1'  # 기본 사이트 url형식
        data = urlencode(wednesday).encode('utf-8')  # urlencode부분에 원하는 요일이 들어가면 됨
        html = Request(url_site, data)
        webpage = urlopen(html).read()
        soup = BeautifulSoup(webpage, "html.parser")  # url에 쿼리를 보내서 내가 원하는 날짜에 해당하는 정보를 크롤링하기!
        # print(soup)

        root = soup.find('td', align='center')
        list_menu_table = root.find_all('table', cellspacing='1')
        list_loc_table = root.find_all('td', class_='menu_st')
        dic = {}
        for i in range(7):
            # print(list_loc_table[i].text.strip())
            lunch = list_menu_table[i].find_all('tr')
            if i == 6:
                # print(lunch[5].text)
                dic[list_loc_table[i].text] = lunch[5].text.split()
            else:
                # print(lunch[1].text)
                dic[list_loc_table[i].text] = lunch[1].text.split()

            # print(list_menu_table[i].text.strip())
        #print(dic)
        #print('=' * 200)
        str = ''
        for i in dic.items():
            # print(i)
            str += i[0] + '-->' + '\n'
            for j in i[1]:
                str += j + '/'
            str += '\n'
        #print(str)

        return JsonResponse({
            'message':{
                'text':str
            },
            'keyboard':{
                'type':'buttons',
                'buttons':['일','월','화','수','목','금','토']
            }
        })
    elif choice=='목':
        url_site = 'https://dgucoop.dongguk.edu/store/store.php?w=4&l=1'  # 기본 사이트 url형식
        data = urlencode(thursday).encode('utf-8')  # urlencode부분에 원하는 요일이 들어가면 됨
        html = Request(url_site, data)
        webpage = urlopen(html).read()
        soup = BeautifulSoup(webpage, "html.parser")  # url에 쿼리를 보내서 내가 원하는 날짜에 해당하는 정보를 크롤링하기!
        # print(soup)

        root = soup.find('td', align='center')
        list_menu_table = root.find_all('table', cellspacing='1')
        list_loc_table = root.find_all('td', class_='menu_st')
        dic = {}
        for i in range(7):
            # print(list_loc_table[i].text.strip())
            lunch = list_menu_table[i].find_all('tr')
            if i == 6:
                # print(lunch[5].text)
                dic[list_loc_table[i].text] = lunch[5].text.split()
            else:
                # print(lunch[1].text)
                dic[list_loc_table[i].text] = lunch[1].text.split()

            # print(list_menu_table[i].text.strip())
        #print(dic)
        #print('=' * 200)
        str = ''
        for i in dic.items():
            # print(i)
            str += i[0] + '-->' + '\n'
            for j in i[1]:
                str += j + '/'
            str += '\n'
        #print(str)

        return JsonResponse({
            'message':{
                'text':str
            },
            'keyboard':{
                'type':'buttons',
                'buttons':['일','월','화','수','목','금','토']
            }
        })
    elif choice=='금':
        url_site = 'https://dgucoop.dongguk.edu/store/store.php?w=4&l=1'  # 기본 사이트 url형식
        data = urlencode(friday).encode('utf-8')  # urlencode부분에 원하는 요일이 들어가면 됨
        html = Request(url_site, data)
        webpage = urlopen(html).read()
        soup = BeautifulSoup(webpage, "html.parser")  # url에 쿼리를 보내서 내가 원하는 날짜에 해당하는 정보를 크롤링하기!
        # print(soup)

        root = soup.find('td', align='center')
        list_menu_table = root.find_all('table', cellspacing='1')
        list_loc_table = root.find_all('td', class_='menu_st')
        dic = {}
        for i in range(7):
            # print(list_loc_table[i].text.strip())
            lunch = list_menu_table[i].find_all('tr')
            if i == 6:
                # print(lunch[5].text)
                dic[list_loc_table[i].text] = lunch[5].text.split()
            else:
                # print(lunch[1].text)
                dic[list_loc_table[i].text] = lunch[1].text.split()

            # print(list_menu_table[i].text.strip())
        #print(dic)
        #print('=' * 200)
        str = ''
        for i in dic.items():
            # print(i)
            str += i[0] + '-->' + '\n'
            for j in i[1]:
                str += j + '/'
            str += '\n'
        #print(str)

        return JsonResponse({
            'message':{
                'text':str
            },
            'keyboard':{
                'type':'buttons',
                'buttons':['일','월','화','수','목','금','토']
            }
        })
    else:
        url_site = 'https://dgucoop.dongguk.edu/store/store.php?w=4&l=1'  # 기본 사이트 url형식
        data = urlencode(saturday).encode('utf-8')  # urlencode부분에 원하는 요일이 들어가면 됨
        html = Request(url_site, data)
        webpage = urlopen(html).read()
        soup = BeautifulSoup(webpage, "html.parser")  # url에 쿼리를 보내서 내가 원하는 날짜에 해당하는 정보를 크롤링하기!
        # print(soup)

        root = soup.find('td', align='center')
        list_menu_table = root.find_all('table', cellspacing='1')
        list_loc_table = root.find_all('td', class_='menu_st')
        dic = {}
        for i in range(7):
            # print(list_loc_table[i].text.strip())
            lunch = list_menu_table[i].find_all('tr')
            if i == 6:
                # print(lunch[5].text)
                dic[list_loc_table[i].text] = lunch[5].text.split()
            else:
                # print(lunch[1].text)
                dic[list_loc_table[i].text] = lunch[1].text.split()

            # print(list_menu_table[i].text.strip())
        #print(dic)
        #print('=' * 200)
        str = ''
        for i in dic.items():
            # print(i)
            str += i[0] + '-->' + '\n'
            for j in i[1]:
                str += j + '/'
            str += '\n'
        #print(str)

        return JsonResponse({
            'message':{
                'text':str
            },
            'keyboard':{
                'type':'buttons',
                'buttons':['일','월','화','수','목','금','토']
            }
        })
