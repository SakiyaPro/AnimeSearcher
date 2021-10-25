from django.shortcuts import render
from django.template.response import TemplateResponse

from .models import AnimeData
from accounts.models import User


def search_home(request):
    '''ホーム画面
    '''
    return TemplateResponse(request, "search_home.html")


def genre_search(request, genre):
    ''' genre_search/<genre> の<genre>に該当するhtmlをレスポンス
        例：<genre>が「Kandou」の場合、「Kandou.html」をレスポンス
    '''

    if genre == "Kandou":
        anime_data = AnimeData.objects.filter(tags__name__in=["感動"]).all()
        anime_data = [anime.to_dict() for anime in anime_data]

    return TemplateResponse(request, 'genre_search/genre_search.html',
                            {
                                "anime_data": anime_data,
                            })
