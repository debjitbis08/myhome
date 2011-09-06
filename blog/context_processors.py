from django.conf import settings
from django.core.cache import cache
from datetime import datetime
import twitter

def env(request):
    if settings.DEBUG:
        return {'env':'DESIGN'}
    else:
        return {'env':request.GET.get('env','BASE')}    

def latest_tweets(request):
    tweet = cache.get('tweet')

    if tweet:
        return {'tweet': tweet}

    try:
        tweet = twitter.Api().GetUserTimeline(settings.TWITTER_USER)[0:8]
    except Exception:
        pass

    cache.set( 'tweet', tweet, settings.TWITTER_TIMEOUT )

    return {"tweet": tweet}
