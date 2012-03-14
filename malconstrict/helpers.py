import json
import malconstrict.models as models
import malconstrict.constants as constants


"""This module contains helper functions for JSON to Model conversion, 
sorting, searching, and more."""


def json_to_anime(data):
    """Transforms a JSON blob to an Anime object.

    Keyword arguments:
    data -- the json blob
    """
    anime = models.Anime()
    d = json.loads(data)
    for key in d.keys():
        setattr(anime, key, d[key])
    return anime


def json_to_list_of_anime(data):
    """Transforms a JSON blob to a list of Anime objects.

    Keyword arguments:
    data -- the json blob
    """
    anime_list = []
    entries = json.loads(data)
    for entry in entries:
        temp_anime = models.Anime()
        for key in entry.keys():
            setattr(temp_anime, key, entry[key])
        anime_list.append(temp_anime)
    return anime_list


def json_to_anime_list(data):
    """Transforms a JSON blob to an AnimeList object.

    Keyword arguments:
    data -- the json blob
    """
    anime_list = models.AnimeList()
    anime_list.anime = []
    d = json.loads(data)
    entries = d['anime']
    anime_list.statistics = d['statistics']

    for entry in entries:
        anime = models.Anime()
        for key in entry.keys():
            setattr(anime, key, entry[key])
        anime_list.anime.append(anime)
    return anime_list


def json_to_manga(data):
    """Transforms a JSON blob to a Manga object.

    Keyword arguments:
    data -- the json blob
    """
    manga = models.Manga()
    d = json.loads(data)
    for key in d.keys():
        setattr(manga, key, d[key])
    return manga


def json_to_list_of_manga(data):
    """Transforms a JSON blob to a list of Manga objects.

    Keyword arguments:
    data -- the json blob
    """
    manga_list = []
    entries = json.loads(data)
    for entry in entries:
        temp_manga = models.Manga()
        for key in entry.keys():
            setattr(temp_manga, key, entry[key])
        manga_list.append(temp_manga)
    return manga_list


def json_to_manga_list(data):
    """Transforms a JSON blob to a MangaList object.

    Keyword arguments:
    data -- the json blob
    """
    manga_list = models.MangaList()
    manga_list.manga = []
    d = json.loads(data)
    entries = d['manga']
    manga_list.statistics = d['statistics']

    for entry in entries:
        manga = models.Manga()
        for key in entry.keys():
            setattr(manga, key, entry[key])
        manga_list.manga.append(manga)
    return manga_list


# unsectioned sort among all entries
def sort_anime(anime_list, how='title', descending=False):
    lst = []
    if isinstance(anime_list, models.AnimeList):
        lst = anime_list.anime
    else:
        lst = anime_list
    
    if how == 'popularity':
        lst.sort(key=lambda a: a.popularity_rank, reverse=descending)
    elif how == 'title':
        lst.sort(key=lambda a: a.title.lower(), reverse=descending)
    elif how == 'members_score':
        lst.sort(key=lambda a: a.members_score, reverse=descending)
    elif how == 'score':
        lst.sort(key=lambda a: a.score, reverse=descending)


# returns a dictionary, sectioned sorts
def sort_anime_sectional(anime_list, how='title', descending=False):
    lst = []
    if isinstance(anime_list, models.AnimeList):
        lst = anime_list.anime
    else:
        lst = anime_list
    
    lists = {}
    lists['watching'] = []
    lists['completed'] = []
    lists['on-hold'] = []
    lists['dropped'] = []
    lists['plan to watch'] = []
    
    sort_anime(lst, how, descending)
    
    for entry in lst:
        if entry.watched_status == 'watching' or entry.watched_status == constants.WATCHING:
            lists['watching'].append(entry)
        elif entry.watched_status == 'completed' or entry.watched_status == constants.COMPLETED:
            lists['completed'].append(entry)
        elif entry.watched_status == 'on-hold' or entry.watched_status == constants.ON_HOLD:
            lists['on-hold'].append(entry)
        elif entry.watched_status == 'dropped' or entry.watched_status == constants.DROPPED:
            lists['dropped'].append(entry)
        elif entry.watched_status == 'plan to watch' or entry.watched_status == constants.PLAN_TO_WATCH:
            lists['plan to watch'].append(entry)
    
    return lists


def search_substring(substr, anime_list):
    lst = []
    if isinstance(anime_list, models.AnimeList):
        lst = anime_list.anime
    else:
        lst = anime_list
    
    ret = []
    for entry in lst:
        if entry.title.lower().find(substr.lower()) != -1:
            ret.append(entry)
    
    sort_anime(ret)
    return ret
    

