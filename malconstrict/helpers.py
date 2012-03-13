import json
import malconstrict.models


"""This module contains helper functions for JSON to Model conversion."""


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
