import models
import helpers

import urllib2

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
    anime_id -- the id of the anime whose details are requested
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
        response = requests.get(apiurl + '/anime/' + str(anime_id) + '?mine=' + str(mine), auth=auth_token)
    else:
        response = requests.get(apiurl + '/anime/' + str(anime_id) + '?mine=' + str(mine))
    return response.content


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
    response = requests.get(apiurl + '/anime/search?q=' + urllib2.quote(query))
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


def raw_get_manga_details(manga_id, mine=0, auth_token=None):
    """Fetch an manga with the given anime id. This returns a manga.
    This is a 'raw' function and will spit out JSON!

    Keyword arguments:
    manga_id -- the id of the manga whose details are requested
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
        response = requests.get(apiurl + '/manga/' + str(manga_id) + '?mine=' + str(mine), auth=auth_token)
    else:
        response = requests.get(apiurl + '/manga/' + str(manga_id) + '?mine=' + str(mine))
    return response.content


def raw_search_manga(query):
    """Search for manga matching a query. The response is a manga.
    
    Keyword arguments:
    query -- The query to send to MAL's search
    """
    response = requests.get(apiurl + '/manga/search?q=' + urllib2.quote(query))
    return response.content


def get_anime_list(username):
    raw = raw_get_anime_list(username)
    return helpers.json_to_anime_list(raw)


def get_anime_details(anime_id, mine=0, auth_token=None):
    raw = raw_get_anime_details(anime_id, mine=mine, auth_token=auth_token)
    return helpers.json_to_anime(raw)


def search_anime(query):
    raw = raw_search_anime(query)
    return helpers.json_to_list_of_anime(raw)


def get_manga_list(username):
    raw = raw_get_manga_list(username)
    return helpers.json_to_manga_list(raw)


def get_manga_details(manga_id, mine=0, auth_token=None):
    raw = raw_get_manga_details(manga_id, mine=mine, auth_token=auth_token)
    return helpers.json_to_manga(raw)


def search_manga(query):
    raw = raw_search_manga(query)
    return helpers.json_to_list_of_manga(raw)


def add_anime_entry(anime_id, auth_token, status=1, episodes=0, score=None):
    payload = {'anime_id': anime_id, 'status': status, 'episodes': episodes}
    if score != None:
        payload['score'] = score
    response = requests.post(apiurl + '/animelist/anime', data=payload, auth=auth_token)


def update_anime_entry(anime_id, auth_token, status=1, episodes=0, score=None):
    payload = {'anime_id': anime_id, 'status': status, 'episodes': episodes}
    if score != None:
        payload['score'] = score
    response = requests.put(apiurl + '/animelist/anime/' + str(anime_id), data=payload, auth=auth_token)


def delete_anime_entry(anime_id, auth_token):
    response = requests.delete(apiurl + '/animelist/anime/' + str(anime_id), auth=auth_token)
    #TODO: Return an actual instance of the appropriate model here
    return response


def add_manga(manga_id, auth_token, status=1, chapters=0, volumes=0, score=None):
    payload = {'manga_id': manga_id, 'status': status, 'chapters': chapters, 'volumes': volumes}
    if score != None:
        payload['score'] = score
    response = requests.post(apiurl + '/mangalist/manga', data=payload, auth=auth_token)


def update_manga_entry(manga_id, auth_token, status=0, chapters=0, volumes=0, score=None):
    payload = {'manga_id': manga_id, 'status': status, 'chapters': chapters, 'volumes': volumes}
    if score != None:
        payload['score'] = score
    response = requests.put(apiurl + '/mangalist/manga/' + str(manga_id), data=payload, auth=auth_token)
    # TODO: Return an actual isntance of the appropriate model here


def delete_manga_entry(manga_id, auth_token):
    response = requests.delete(apiurl + '/mangalist/manga/' + str(manga_id), auth=auth_token)
    #TODO: Return an actual instance of the appropriate model here
    return response


def verify_credentials(auth_token):
    response = requests.get(apiurl + '/account/verify_credentials', auth=auth_token)
    return response