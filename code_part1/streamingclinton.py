#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os

#Variables that contains the user credentials to access Twitter API
access_token = os.environ.get('TWITTER_ACCESS_KEY')
access_token_secret = os.environ.get('TWITTER_SECRET_ACCESS_KEY')
consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_SECRET_CONSUMER_KEY')


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    try:

        #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
        stream.filter(track=['#clintonkaine2016', '#dumptrump','#fucktrump',
                          '#givethemhill','#hillary2016','#hillaryforamerica','#hillaryforpresident',
                          '#imwithher','#latinosforhillary','#lovetrumpshate','#madampresident',
                          '#makedonalddrumpfagain','#nastywoman', '#clinton2016'
                          '#nevertrump', '#badhombres','#sheswithus','#shewon','#strongertogether',
                          '#voteclintonkaine2016', '#womenforhillary','bad hombre',
                          "i'm with her",'im with her', 'nasty woman','nasty women',
                          'stronger together','strongertogether',
                           '#IAmWithHer', '#uniteblue'])

    except KeyboardInterrupt:
        pass
