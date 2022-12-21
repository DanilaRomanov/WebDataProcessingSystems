import requests
from mwviews.api import PageviewsClient

p = PageviewsClient("https://www.mediawiki.org/wiki/REST_API")


def _get_wikipedia_articles(named_entity):
    # Set the endpoint for the Wikipedia API
    endpoint = "https://en.wikipedia.org/w/api.php"

    # Set the parameters for the API call
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": named_entity,
        "utf8": 1,
        "formatversion": 2,
        "formatversion": 2,
    }

    # Make the API call
    r = requests.get(endpoint, params=params)

    # Extract the list of articles from the response
    articles = r.json()["query"]["search"]

    # Create a list of links to the articles
    links = []
    for article in articles:
        title = article["title"]
        links.append(title)
        # title = title.replace(" ", "_")
        # link = f"https://en.wikipedia.org/wiki/{title}"
        # links.append(link)

    # Return the list of links
    # Return time taken for this function

    return links


def _select_most_popular(views):
    max_views = 0
    max_key = ""
    dct = list(views.values())[0]
    keys = list(dct.keys())
    # Get key with max value
    for key in keys:
        if not dct[key]:
            continue
        if int(dct[key]) > max_views:
            max_views = int(dct[key])
            max_key = key
    return max_key


def link_entity(entity):
    articles = _get_wikipedia_articles(entity)
    if articles == []:
        return None
    try:
        views = p.article_views(
            "en.wikipedia",
            articles,
            granularity="monthly",
            start="2022100100",
            end="2022103100",
        )
    except:
        print("No entity found test")
        return None
    if len(views) == 0:
        print("No entity found")
        return None
    top_ambiguity = _select_most_popular(views)
    return f"https://en.wikipedia.org/wiki/{top_ambiguity}"
