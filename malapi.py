import requests
from requests.auth import HTTPBasicAuth


apiurl = 'http://mal-api.com'

def raw_get_anime_list(username):
    response = requests.get(apiurl + '/animelist/' + username)
    return response.content

def raw_get_anime_details(id):
    response = requests.get(apiurl + '/anime/' + str(id))
    return response.content

def raw_get_history(username):
    response = requests.get(apiurl + '/history/' + username)
    return response.content

def raw_search_anime(query):
    response = requests.get(apiurl + '/anime/search?q=' + query)
    return response.content

def raw_get_popular():
    response = requests.get(apiurl + '/popular')
    return response.content

def raw_get_upcoming():
    response = requests.get(apiurl + '/upcoming')
    return response.content

def raw_get_just_added():
    response = requests.get(apiurl + '/just_added')
    return response.content

def raw_get_manga_list(username):
    response = requests.get(apiurl + '/mangalist/' + username)
    return response.content

def raw_get_manga_details(id):
    response = requests.get(apiurl + '/manga/' + str(id))
    return response.content

def raw_search_manga(query):
    response = requests.get(apiurl + '/manga/search?q=' + query)
    return response.content