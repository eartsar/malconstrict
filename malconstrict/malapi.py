import malconstrict.models
import malconstrict.helpers
import malconstrict.exceptions

import urllib2
import requests


"""
This is the main API wrapping module of malconstrict. All 'raw' functions
should only be called if JSON is required as the output.
"""

apiurl = 'http://mal-api.com'


def raw_get_anime_list(username):
    """Fetch an anime list with the given username.
    This is a 'raw' function and will spit out JSON!

    Keyword arguments:
    username -- the name of the user whose anime list is requested
    """
    response = requests.get(apiurl + '/animelist/' + username)
    if response.status_code == 500:
        raise exceptions.UserNotFoundException()
    return response.content


def raw_get_anime_details(anime_id, mine=0, auth_token=None):
    """Fetch an anime with the given anime id. This returns an anime.
    This is a 'raw' function and will spit out JSON!

    Keyword arguments:
    anime_id -- the id of the anime whose details are requested
    mine -- if 1, reflects user's data. Requires an auth_token (default 0)
    auth_token -- a two value tuple that defines the (user, password)
    """
    response = None
    if mine == 1:
        if not isinstance(auth_token, tuple):
            raise exception.BadAuthenticationException()
        response = requests.get(
                apiurl + '/anime/' + str(anime_id) + '?mine=' + str(mine),
                auth=auth_token
        )
    else:
        response = requests.get(
            apiurl + '/anime/' + str(anime_id) + '?mine=' + str(mine))

    if response.status_code == 404:
        raise exceptions.EntryNotFoundException()
    return response.content


def raw_get_history(username):
    """NOT YET IMPLEMENTED!

    Fetch the history of a user with the given username

    Keyword arguments:
    username -- the name of the user whose history is being queried
    """
    raise NotYetImplementedException()

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
    """NOT YET IMPLEMENTED!

    Fetch the top anime.
    """
    raise NotYetImplementedException()

    response = requests.get(apiurl + '/top')
    return response.content


def raw_get_popular():
    """NOT YET IMPLEMENTED!

    Fetch the recent popular anime.
    """
    raise NotYetImplementedException()

    response = requests.get(apiurl + '/popular')
    return response.content


def raw_get_upcoming():
    """NOT YET IMPLEMENTED!

    Fetch the upcoming anime sorted by airing date.
    """
    raise NotYetImplementedException()

    response = requests.get(apiurl + '/upcoming')
    return response.content


def raw_get_just_added():
    """NOT YET IMPLEMENTED!

    Fetch the anime that have just been added to the MAL database.
    """
    raise NotYetImplementedException()

    response = requests.get(apiurl + '/just_added')
    return response.content


def raw_get_manga_list(username):
    """Fetch a manga list with the given username.
    This is a 'raw' function and will spit out JSON!

    Keyword arguments:
    username -- the name of the user whose manga list is requested
    """
    response = requests.get(apiurl + '/mangalist/' + username)
    if response.status_code == 500:
        raise exceptions.UserNotFoundException()
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
            raise exceptions.BadAuthenticationException()
        response = requests.get(
            apiurl + '/manga/' + str(manga_id) + '?mine=' + str(mine),
            auth=auth_token
        )
    else:
        response = requests.get(
            apiurl + '/manga/' + str(manga_id) + '?mine=' + str(mine))

    if response.status_code == 404:
        raise exceptions.EntryNotFoundException()
    return response.content


# TODO: exceptions
def raw_search_manga(query):
    """Search for manga matching a query. The response is a manga.
    This is a 'raw' function and will spit out JSON!

    Keyword arguments:
    query -- The query to send to MAL's search
    """
    response = requests.get(apiurl + '/manga/search?q=' + urllib2.quote(query))
    return response.content


def get_anime_list(username):
    """Fetch an anime list with the given username. This returns an AnimeList
    object defined in malconstrict.models .

    Keyword arguments:
    username -- the username whose list is to be fetched
    """
    raw = raw_get_anime_list(username)
    return helpers.json_to_anime_list(raw)


def get_anime_details(anime_id, mine=0, auth_token=None):
    """Fetch an anime with the given anime id. This returns an Anime object
    defined in malconstrict.models .

    Keyword arguments:
    anime_id -- the id of the anime to be queried
    mine -- if 1, reflects user's data. Requires an auth_token (default 0)
    auth_token -- a two value tuple that defines the (user, password)
    """
    raw = raw_get_anime_details(anime_id, mine=mine, auth_token=auth_token)
    return helpers.json_to_anime(raw)


def search_anime(query):
    """Search for anime matching a query.

    Keyword arguments:
    query -- The query. This is encoded internally SO NO WORRIES I HOPE!
    """
    raw = raw_search_anime(query)
    return helpers.json_to_list_of_anime(raw)


def get_manga_list(username):
    """Fetch a manga list with the given username.

    Keyword arguments:
    username -- the name of the user whose manga list is requested
    """
    raw = raw_get_manga_list(username)
    return helpers.json_to_manga_list(raw)


def get_manga_details(manga_id, mine=0, auth_token=None):
    """Fetch an manga with the given anime id. This returns a manga.

    Keyword arguments:
    manga_id -- the id of the manga whose details are requested
    mine -- if 1, reflects user's data. Requires an auth_token. (default 0)
    auth_token -- a two value tuple that defines the (user, password)
    """
    raw = raw_get_manga_details(manga_id, mine=mine, auth_token=auth_token)
    return helpers.json_to_manga(raw)


def search_manga(query):
    """Search for manga matching a query. The response is a manga.

    Keyword arguments:
    query -- The query to send to MAL's search
    """
    raw = raw_search_manga(query)
    return helpers.json_to_list_of_manga(raw)


# TODO: exceptions
def add_anime_entry(anime_id, auth_token, status=1, episodes=0, score=None):
    """Adds an anime to a user's anime list:

    Keyword arguments:
    anime_id -- the id of the anime whose details are requested
    auth_token -- a two value tuple that defines the (user, password)
    status -- the status of the anime (check malconstrict.constants, default=1)
    episodes -- the number of episodes seen (default=0)
    score -- the score given (default=None)
    """
    payload = {'anime_id': anime_id, 'status': status, 'episodes': episodes}
    if score != None:
        payload['score'] = score
    response = requests.post(
        apiurl + '/animelist/anime', data=payload, auth=auth_token)


# TODO: exceptions
def update_anime_entry(anime_id, auth_token, status=1, episodes=0, score=None):
    """Updates an anime already on a user's anime list.

    Keyword arguments:
    anime_id -- the id of the anime whose details are requested
    auth_token -- a two value tuple that defines the (user, password)
    status -- the status of the anime (check malconstrict.constants, default=1)
    episodes -- the number of episodes seen (default=0)
    score -- the score given (default=None)
    """
    payload = {'anime_id': anime_id, 'status': status, 'episodes': episodes}
    if score != None:
        payload['score'] = score
    response = requests.put(
            apiurl + '/animelist/anime/' + str(anime_id),
            data=payload,
            auth=auth_token
    )


def delete_anime_entry(anime_id, auth_token):
    """Delete an anime from a user's anime list. This removes any record of the
    anime from a user's anime list and connot be undone.

    Keyword arguments:
    anime_id -- the id of the anime to be removed
    auth_token -- a two value tuple that defines the (user, password)
    """
    response = requests.delete(
            apiurl + '/animelist/anime/' + str(anime_id), auth=auth_token)

    if response.status_code == 401:
        raise exceptions.BadAuthenticationException()
    elif response.status_code == 404:
        raise exceptions.EntryNotFoundException()
    elif response.status_code == 500:
        raise exceptions.NotInListException()


# TODO: exceptions
def add_manga(
    manga_id, auth_token, status=1, chapters=0, volumes=0, score=None):
    """Adds an manga to a user's manga list.

    Keyword arguments:
    manga_id -- the id of the manga whose details are requested
    auth_token -- a two value tuple that defines the (user, password)
    status -- the status of the manga (check malconstrict.constants, default=1)
    chapters -- the number of chapters read (default=0)
    volumes -- the number of volumes read (default=0)
    score -- the score given (default=None)
    """
    payload = {
        'manga_id': manga_id,
        'status': status,
        'chapters': chapters,
        'volumes': volumes
    }
    if score != None:
        payload['score'] = score
    response = requests.post(
            apiurl + '/mangalist/manga', data=payload, auth=auth_token)


# TODO: exceptions
def update_manga_entry(manga_id, auth_token, status=0,
                       chapters=0, volumes=0, score=None):
    """Updates a manga already on a user's manga list.

    Keyword arguments:
    manga_id -- the id of the manga whose details are requested
    auth_token -- a two value tuple that defines the (user, password)
    status -- the status of the manga (check malconstrict.constants, default=1)
    chapters -- the number of chapters read (default=0)
    volumes -- the number of volumes read (default=0)
    score -- the score given (default=None)
    """
    payload = {
        'manga_id': manga_id,
        'status': status,
        'chapters': chapters,
        'volumes': volumes
    }
    if score != None:
        payload['score'] = score
    response = requests.put(
                apiurl + '/mangalist/manga/' + str(manga_id),
                data=payload,
                auth=auth_token
    )


def delete_manga_entry(manga_id, auth_token):
    """Delete a manga from a user's manga list. This removes any record of the
    manga from a user's manga list and connot be undone.

    Keyword arguments:
    manga_id -- the id of the manga to be removed
    auth_token -- a two value tuple that defines the (user, password)
    """

    response = requests.delete(
            apiurl + '/mangalist/manga/' + str(manga_id), auth=auth_token)

    if response.status_code == 401:
        raise exceptions.BadAuthenticationException()
    elif response.status_code == 404:
        raise exceptions.EntryNotFoundException()
    elif response.status_code == 500:
        raise exceptions.NotInListException()


def verify_credentials(auth_token):
    """Test whether supplied user credentials are valid.
    The authentication mechanism is HTTP Basic Authentication.

    Keyword arguments:
    auth_token -- the authentication token to be used for verification
    """
    response = requests.get(
            apiurl + '/account/verify_credentials', auth=auth_token)
    if response.status_code == 200:
        print "Authentication Successful"
    elif response.status_code == 401:
        print "Authentication Failed"
