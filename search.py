# -*- coding: UTF-8 -*-
from googlesearch import search
import re

def searchByGoogle (query): 

    url = None
    website = None

# using google search find url
    for j in search(query, num=5, stop=20, pause=1): 
        url = j
        if (re.search(r"dmm.com",j)) :
            website = "dmm.com"
            break
        elif(re.search(r"avgle.com",j)) :
            website = "avgle.com"
            break
        else :
            continue

# format return object
    obj = {}
    obj['website'] = website
    obj['url'] = url
    obj['fileName'] = query


    return obj


print(searchByGoogle('snis-609'))



    
    






















"""
    # query: Query string. Must NOT be url-encoded.
    # tld: Top level domain.
    # lang: Language.
    # tbs: Time limits (i.e "qdr:h" => last hour,"qdr:d" => last 24 hours, "qdr:m" => last month).
    # safe: Safe search.
    # int num: Number of results per page.
    # int start: First result to retrieve.
    # int or None stop: Last result to retrieve.Use None to keep searching forever.
    # list of str or None domains: A list of web domains to constrain the search.
    # float pause: Lapse to wait between HTTP requests.    A lapse too long will make the search slow, but a lapse too short may cause Google to block your IP. Your mileage may vary!
    bool only_standard: If True, only returns the standard results from
        each page. If False, it returns every possible link from each page,
        except for those that point back to Google itself. Defaults to False
        for backwards compatibility with older versions of this module.
    dict of str to str extra_params: A dictionary of extra HTTP GET
        parameters, which must be URL encoded. For example if you don't want
        Google to filter similar results you can set the extra_params to
        {'filter': '0'} which will append '&filter=0' to every query.
    Search type (images, videos, news, shopping, books, apps)
        Use the following values {videos: 'vid', images: 'isch',
        news: 'nws', shopping: 'shop', books: 'bks', applications: 'app'}
    or None user_agent: User agent for the HTTP requests.
        Use None for the default.
"""
    