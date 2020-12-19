#!/usr/bin/env python
import sys
import requests
import os
from flask import Flask, request
import redis
import hashlib
import base64

SUCCESS = "Success"


#Environment variable consts
REDIS_URL='REDIS_URL'

#constants
HASH_NAME = 'hashUrl'
APPEND_URL = '**'

REQ_CONFIG_VARS = [REDIS_URL]

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)



def validate_env():
    for field in REQ_CONFIG_VARS:
        if field not in os.environ:
            raise ConfigVarsMissingError(
                "Failed to create app instance due to missing %s", field
            )



def get_reddis_con():
    try:
        redis_url = os.environ[REDIS_URL]
        redis_conn = redis.from_url(redis_url)
        #redis_conn=redis.Redis() # for running in local machne use this this line
        return redis_conn
    except KeyError as err:
        LOGGER.error("Failed to create Redis connection, aborting, error %s", err)




def create_hash_for_url(url):
    result = hashlib.md5(url.encode('utf-8'))
    data = str(result.hexdigest())
    encodedBytes = base64.b64encode(data.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    first_six_char = encodedStr[:6]
    print(first_six_char)
    return first_six_char


def handle_hash_collision(actual_url , redis_conn):
    hash_of_url = create_hash_for_url(actual_url)
    check = redis_conn.hexists(HASH_NAME, hash_of_url)
    if (check):
        url = redis_conn.hget(HASH_NAME, hash_of_url).decode('utf-8')
        if actual_url == url:
            return hash_of_url
        else:
            return handle_hash_collision(actual_url + APPEND_URL , redis_conn)
    else:
        return hash_of_url



def create_app():
    app = Flask('News-Byte-Url-service')
    redis_conn = get_reddis_con()


    @app.route('/hashUrl' ,methods=['POST'])
    def hashUrl():
        req_data = request.get_json()
        url = str (req_data['url'])
        hash = handle_hash_collision(url ,redis_conn)
        redis_conn.hset(HASH_NAME, hash, url)
        return app.make_response((hash, requests.codes.OK))

    @app.route('/getHash' ,methods=['POST'])
    def getHash():
        req_data = request.get_json()
        hash_of_url = req_data["hash_of_url"]
        redis_conn.hget(HASH_NAME, hash_of_url)
        check = redis_conn.hexists(HASH_NAME, hash_of_url)
        if (check):
            url = redis_conn.hget(HASH_NAME, hash_of_url)
            return url
        else:
            return "Invalid hash"


    @app.route('/status')
    def status_check():
        return app.make_response((SUCCESS, requests.codes.OK))

    return app
