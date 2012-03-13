import json
import inspect
import malapi as mal
import models

def json_to_anime(data):
    anime = models.Anime()
    d = json.loads(data)
    members = inspect.getmembers(anime)
    for key in d.keys():
        setattr(anime, key, d[key])
    return anime


def json_to_anime_list(data):
    anime_list = models.AnimeList()
    d = json.loads(data)
    members = inspect.getmembers(anime_list)
    for key in d.keys():
        setattr(anime_list, key, d[key])
    return anime_list


def json_to_manga(data):
    manga = models.Manga()
    d = json.loads(data)
    members = inspect.getmembers(manga)
    for key in d.keys():
        setattr(manga, key, d[key])
    return manga


def json_to_manga_list(data):
    manga_list = models.AnimeList()
    d = json.loads(data)
    members = inspect.getmembers(manga_list)
    for key in d.keys():
        setattr(manga_list, key, d[key])
    return manga_list