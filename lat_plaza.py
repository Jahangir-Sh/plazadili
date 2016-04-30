import os
import json
import datetime
from itertools import starmap
from tweepy import OAuthHandler, API
import settings


def get_statuses():
    api = API(OAuthHandler(*starmap(os.environ.get, settings.CONFIG)))
    topics = ("#plazadili", "plazadili")

    with open(os.path.join(settings.BASE_DIR, datetime.datetime.now().isoformat() + ".json"), "w+") as jsn:
        json.dump(
            {"data": [{"user": tweet.user.screen_name, "text": tweet.text} for tweet in api.search(",".join(topics))]},
            jsn, ensure_ascii=False, indent=4
        )
