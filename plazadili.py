import os
import json
import subprocess
from datetime import datetime
from itertools import starmap
from tweepy import OAuthHandler, API
import settings


def get_statuses():
    api = API(OAuthHandler(*starmap(os.environ.get, settings.CONFIG)))
    topics = ("#plazadili", "plazadili")

    with open(os.path.join(settings.DATA_DIR, datetime.now().isoformat() + ".json"), "w+") as jsn:
        json.dump(
            {"data": [{"user": tweet.user.screen_name, "text": tweet.text} for tweet in api.search(",".join(topics))]},
            jsn, ensure_ascii=False, indent=4
        )

if __name__ == "__main__":
    get_statuses()

    os.chdir(settings.BASE_DIR)
    commands = map(str.split, [
        "git add .",
        "git commit -am \"{}\"".format(datetime.now().isoformat()),
        "git push plaza data"
    ])

    map(subprocess.call, commands)
