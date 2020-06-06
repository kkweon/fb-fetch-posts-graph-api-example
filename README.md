# Fetch posts with likes using Facebook Graph API

1. Prepare environment variables
```shell script
export FB_GROUP_ID=292278624537271
export FB_ACCESS_TOKEN=EAANgaLtKoyWfCAVRYf34pi
```

2. Run 

```shell script
pipenv run python main.py
```

```shell script
pipenv run python main.py
Loading .env environment variables…
Warning: There was an unexpected error while activating your virtualenv. Continuing anyway...

[
Message(message=안녕하세요....., likes=[Like(id=10163522886740632, name=Mo Kweon, type=LIKE)], updated_time=2017-07-30 02:58:12+00:00, id=292278624537271_347260859039047), 
Message(message=윤석찬 님께서..., likes=[Like(id=10163522886740632, name=Mo Kweoe=LIKE)], updated_time=2018-01-17 02:03:50+00:00, id=292278624537271_347940348971098), 
Message(message=텐플코리아가 ..., likes=[Like(id=10163522886740632, name=Mo Kweon, type=LIKE)], updated_time=2017-05-27 18:21:01+00:00, id=292278624537271_317699918661808), 
]
```
