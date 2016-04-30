import os
import json
import datetime
from itertools import starmap
from tweepy import OAuthHandler, API

CONFIG = (
    ("CONSUMER_TOKEN", "DSKLZ2luVXAT5gxoJjAYYirB7"),
    ("CONSUMER_SECRET", "IaBJSOzn4E4v4Vj4dtrTcaASBuD0Mu6Mj3PPjgaKHvweyhQFPM")
)

api = API(OAuthHandler(*starmap(os.environ.get, CONFIG)))
topics = ("#plazadili", "plazadili")

with open(datetime.datetime.now().isoformat() + ".json", "w+") as jsn:
    json.dump(
        {"data": [{"user": tweet.user.screen_name, "text": tweet.text} for tweet in api.search(",".join(topics))]},
        jsn, ensure_ascii=False
    )
