# Dick Bot
# Desc: I am a bot named Dick, my primary functions are to fuck scammers.

# pre-reqs
import requests
import os
import json


# load config
class myConfig(object):
    def loadConfig(conf):
        # Load config file
        with open(r'confdat.conf', 'r') as cf:
            lines = cf.readlines()
            for row in lines:
                if "apikey" in row:
                    conf.apikeyfind = row[8:]
                    #print(conf.apikeyfind)

                if "apisecret" in row:
                    conf.apisecretfind = row[11:]
                    #print(conf.apisecretfind)

                if "bearer" in row:
                    conf.bearerfind = row[8:]
                    #print(conf.bearerfind)

        return conf.apikeyfind, conf.apisecretfind, conf.bearerfind



# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
apikey,apisecret,bearer = myConfig().loadConfig()
bearer_token = bearer


def create_url():
    # Replace with user ID below
    user_id = 2244994945
    return "https://api.twitter.com/2/users/{}/mentions".format(user_id)


def get_params():
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    return {"tweet.fields": "text"}


def bearer_oauth(r):
    apikey,apisecret,bearer = myConfig().loadConfig()
    bearer = bearer.strip('\n')
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer}"
    r.headers["User-Agent"] = "v2UserMentionsPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()








def fuck():
    # Set config data
    apikey,apisecret,bearer = myConfig().loadConfig()

    # print("apikey:",apikey.strip('\n')) # test successful
    # print("secret:",apisecret.strip('\n')) # test successful
    # print("bearer:",bearer.strip('\n')) # test successful

    url = create_url()
    params = get_params()

    # clean up output
    charWash = ['{', '}', ',', '"']
    translation_table = str.maketrans('', '', ''.join(charWash))

    json_response = connect_to_endpoint(url, params)
    cleanprep = json.dumps(json_response, indent=4, sort_keys=True).translate(translation_table)
    #print(cleanprep)


    prepWashed = cleanprep.translate(translation_table)
    print(prepWashed)

    with open('results.txt', 'w') as f:
        prepcache = json.dumps(json_response, indent=4, sort_keys=True).translate(translation_table)
        f.write(prepcache)
        print(cleanprep)

if __name__ == "__main__":
    fuck()
