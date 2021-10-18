from django.shortcuts import render
from django.template.response import TemplateResponse


def search_home(request):
    '''ホーム画面
    '''
    return TemplateResponse(request, "search_home.html")


def genre_search(request, genre):
    ''' genre_search/<genre> の<genre>に該当するhtmlをレスポンス
        例：<genre>が「Kandou」の場合、「Kandou.html」をレスポンス
    '''
    if genre == "Kandou":
        return TemplateResponse(request, 'genre_search/search_Kandou.html')
