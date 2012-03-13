import models
import helpers

import requests
from requests.auth import HTTPBasicAuth


apiurl = 'http://mal-api.com'


def raw_get_anime_list(username):
    """Fetch an anime list with the given username.
    This is a 'raw' function and will spit out JSON!
    
    Keyword arguments:
    username -- the name of the user whose anime list is requested
    """
    response = requests.get(apiurl + '/animelist/' + username)
    return response.content


def raw_get_anime_details(anime_id, mine=0, auth_token=None):
    """Fetch an anime with the given anime id. This returns an anime.
    This is a 'raw' function and will spit out JSON!
    
    Keyword arguments:
    id -- the id of the anime whose details are requested
    mine -- if 1, reflects user's data. Requires an auth_token. (default 0)
    auth_token -- a two value tuple that defines the (user, password)
    """
    response = None
    if mine == 1:
        if not isinstance(auth_token, tuple):
            # bad auth token exception
            return response
        if len(auth_token) != 2:
            # print bad length error
            return response
        response = requests.get(apiurl + '/anime/' + str(anime_id) + '?mine=' + str(mine), auth_token).content
    else:
        response = requests.get(apiurl + '/anime/' + str(anime_id) + '?mine=' + str(mine)).content
    return response


def raw_get_history(username):
    """NOT YET IMPLEMENTED
    
    Fetch the history of a user with the given username.
    
    Keyword arguments:
    username -- the name of the user whose history is being queried.
    """
    response = requests.get(apiurl + '/history/' + username)
    return response.content


def raw_search_anime(query):
    """Search for anime matching a query. The response is an anime.
    
    Keyword arguments:
    query -- The query to send to MAL's search
    """
    response = requests.get(apiurl + '/anime/search?q=' + query)
    return response.content


def raw_get_top():
    """NOT YET IMPLEMENTED

    Fetch the top anime.
    """
    response = requests.get(apiurl + '/top')
    return response.content


def raw_get_popular():
    """NOT YET IMPLEMENTED
    
    Fetch the recent popular anime.
    """
    response = requests.get(apiurl + '/popular')
    return response.content


def raw_get_upcoming():
    """NOT YET IMPLEMENTED
    
    Fetch the upcoming anime sorted by airing date.
    """
    response = requests.get(apiurl + '/upcoming')
    return response.content


def raw_get_just_added():
    """NOT YET IMPLEMENTED
    
    Fetch the anime that have just been added to the MAL database.
    """
    response = requests.get(apiurl + '/just_added')
    return response.content


def raw_get_manga_list(username):
    """Fetch a manga list with the given username.
    This is a 'raw' function and will spit out JSON!
    
    Keyword arguments:
    username -- the name of the user whose manga list is requested
    """
    response = requests.get(apiurl + '/mangalist/' + username)
    return response.content


def raw_get_manga_details(id, mine=0, auth_token=None):
    """Fetch a manga with the given manga id. This returns a manga.
    This is a 'raw' function and will spit out JSON!
    
    Keyword arguments:
    id -- the id of the manga whose details are requested
    mine -- if 1, reflects user's data. Requires an auth_token. (default 0)
    auth_token -- a two value tuple that defines the (user, password)
    """
    response = None
    if mine == 1:
        if not isinstance(auth_token, tuple):
            # bad auth token exception
            return response
        if len(auth_token) != 2:
            # print bad length error
            return response
        response = requests.get(apiurl + '/manga/' + str(id) + '?mine=' + str(mine), auth_token).content
    else:
        response = requests.get(apiurl + '/manga/' + str(id) + '?mine=' + str(mine)).content
    return response


def raw_search_manga(query):
    """Search for manga matching a query. The response is a manga.
    
    Keyword arguments:
    query -- The query to send to MAL's search
    """
    response = requests.get(apiurl + '/manga/search?q=' + query)
    return response.content


def get_anime_list(username):
    raw = raw_get_anime_list(username)
    return helpers.json_to_anime_list(raw)


def get_anime_details(id, mine=0, auth_token=None):
    raw = raw_get_anime_details(id)
    return helpers.json_to_anime(raw)


def search_anime(query):
    raw = raw_search_anime(query)
    return helpers.json_to_anime_list(raw)


def get_manga_list(username):
    raw = raw_get_manga_list(username)
    return helpers.json_to_manga_list(raw)


def get_manga_details(id, mine=0, auth_token=None):
    raw = raw_get_manga_details(id)
    return helpers.json_to_manga(raw)


def search_manga(query):
    raw = raw_search_manga(query)
    return helpers.json_to_manga_list(raw)