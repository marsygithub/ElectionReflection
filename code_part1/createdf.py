import json
import pandas as pd

def create_dataframe(filename):
    created_at = []
    text = []
    user_created_at = []
    user_screen_name = []
    user_id_str = []
    user_location = []
    user_description = []
    user_followers = []
    user_friends = []
    user_lang = []
    geo = []
    coordinates = []
    rt_user_screen_name = []
    rt_user_location = []
    rt_user_description = []
    rt_count = []
    rt_favorite = []
    hashtags = []
    user_mentions = []

    with open(filename, 'r') as f:

        for line in f:
            line = line.strip(']0;IPython: project/data')
            if line == "\n" or line == "" or line == "\r\n":
                continue
            else:
                tweet = json.loads(line) # load it as Python dict

                if 'limit' in tweet.keys():
                    continue
                else:

                    created_at.append(tweet['created_at'])
                    text.append(tweet['text'].encode('utf-8'))
                    user_created_at.append([tweet['user']['created_at']])
                    user_id_str.append(tweet['user']['id_str'])
                    user_screen_name.append(tweet['user']['screen_name'])
                    user_location.append(tweet['user']['location'])
                    user_description.append(tweet['user']['description'])
                    user_followers.append(tweet['user']['followers_count'])
                    user_friends.append(tweet['user']['friends_count'])
                    user_lang.append(tweet['user']['lang'])

                    geo.append(tweet['geo'])
                    coordinates.append(tweet['coordinates'])

                    if tweet['entities']['hashtags'] != []:
                        items = []
                        for item in tweet['entities']['hashtags']:
                            items.append(item['text'])
                        hashtags.append(items)
                    else:
                        hashtags.append('null')


                    if tweet['entities']['user_mentions'] != []:
                        items = []
                        for item in tweet['entities']['user_mentions']:
                            items.append(item['screen_name'])
                        user_mentions.append(items)
                    else:
                            user_mentions.append('null')

                    if 'retweeted_status' in tweet.keys() == True:
                        rt_user_screen_name.append(tweet['retweeted_status']['user']['screen_name'])
                        rt_user_location.append(tweet['retweeted_status']['user']['location'])
                        rt_user_description.append(tweet['retweeted_status']['user']['description'])
                        rt_count.append(tweet['retweeted_status']['retweet_count'])
                        rt_favorite.append(tweet['retweeted_status']['favorite_count'])
                    else:
                        rt_user_screen_name.append("null")
                        rt_user_location.append("null")
                        rt_user_description.append("null")
                        rt_count.append("null")
                        rt_favorite.append("null")


    df = pd.DataFrame({ 'user_screen_name': user_screen_name, 'user_created_at': user_created_at,
                        'user_id_str': user_id_str, 'text': text, 'user_location': user_location,
                        'user_description': user_description, 'user_followers': user_followers,
                        'user_friends': user_friends, 'user_lang': user_lang, 'geo': geo,
                        'coordinates': coordinates, 'rt_user_screen_name': rt_user_screen_name,
                        'rt_user_location': rt_user_location,'rt_user_description': rt_user_description,
                        'rt_count': rt_count, 'rt_favorite': rt_favorite, 'hashtags': hashtags,
                        'user_mentions': user_mentions})

    df = df[['user_created_at','user_screen_name','user_id_str','text' ,'user_location',
                        'user_description', 'user_followers','user_friends', 'user_lang', 'geo',
                        'coordinates', 'rt_user_screen_name','rt_user_location','rt_user_description',
                        'rt_count', 'rt_favorite', 'hashtags','user_mentions']]

    return df
if __name__ == "__main__":
    df = create_dataframe('politicaltweets.json')
