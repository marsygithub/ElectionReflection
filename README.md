# Election Reflection

![alt text](/images/trump_clinton.png)


## Motivation

The 2016 election was arguably the most controversial election of all time.  

I decided to mine Twitter data as a start since Twitter has so much data processed every minute to see what kind of information I could uncover about the presidential election.

It's easy to get caught up in slogans and catch phrases and fail to hear the actual message of a campaign.  It's easy to remember #nastywoman and #makeamericagreatagain, but most of us won't remember specific policy promises, if there were any at all.  Because of this, I wanted to explore the meat of campaign speeches and identify the topics that each candidate focuses on the most.  

Additionally, I've met many people who regret not voting in the primaries.  The answer is always the same (excluding laziness) - "I didn't know enough about the politicians and didn't feel I could make an educated decision."  This seems to be common so I wanted to design a program that allowed somebody to make an educated decision and direct them to candidates that better reflect their views.  


## Overview

This project is comprised of 3 parts.  

Part 1 explores data collected through the Twitter API.  

Part 2 examines and compares Clinton and Trump campaign speeches.  Bonus: Clintbot and Trumpbot go to Twitter war.  

Part 3 recommends a congress person based on a user's keywords.

## Part 1

### Definitions
Clinton Supporter:  A person who used a hashtag or phrase associated with a Clinton supporter.  Ex. "imwithher" - see `streamingclinton.py`

Trump Supporter:  A person who used a hashtag or phrase associated with a Clinton supporter.  Ex. "makeamericagreatagain" - see `streamingtrump.py`

### The Data
The data was collected from the Twitter streaming API. The files `streamingclinton.py` and `streamingtrump.py` contain the phrases and hasttags that were used to filter the tweets.

I collected tweets for a couple hours everyday for 5 days during the last week of October.  The tweets were stored in a json file and then processed using natural language processing tools and TFIDF.

The tweets were then filtered to users who had active Twitter accounts before 2016 and who posted fewer than 20 times over the 5 day collection period.  My goal was to eliminate the "crazies" and get a more accurate representation of a typical Clinton tweeter and typical Trump tweeter.  


### Observations
Twitter data is incredibly messy and twitter users tend to use hashtags generously.  A hashtag is not always a good indication that a person is a Clinton or Trump supporter.

For the same time period I collected 5.70 GB of data for Trump and 1.34 GB of data for Clinton.

Twitter allows its users to write their own user descriptions.  The following wordclouds were produced from Clinton supporter's user descriptions and Trump supporter's user descriptions.  
![alt text](/images/combined_twitter.png)

Even though Clinton and Trump supporters have drastically different views, the way a person describes him/herself is surprisingly similar.  It is also surprising that with all the hateful election rhetoric floating around on Twitter that the most common used word in a user description is actually "love."




## Part 2

### The Data

#### Speeches and Debates
Campaign speeches and presidential debates were used in doing this analysis.

The speeches and debate transcripts were collected from a variety of sources:
  - www.hillaryclinton.com/speeches
  - www.whatthefolly.com
  - www.time.com
  - www.newsweek.com
  - www.nytimes.com

All speeches collected were given in 2016.  

It is also important to note that the official Trump campaign site did not publish Trump's actual campaign speeches so all of Trump's speeches came from third party sources.


#### Tweets
Additionaly, I collected 3,200 (Twitter's max from the REST API) historical tweets from Clinton and Trump and saved the hashtags.  

#### User Tags
The screen names from Clinton tweeters and Trump tweeters were stored in a separate file from part 1.


### Wordclouds
The following wordclouds represent the most commonly used words in the campaign speeches.  The top two charts have no filtering and the bottom two charts only pull adjectives and nouns and eliminate the most commonly used words such as "people" and "American".
![alt text](/images/wordclouds.png)



### Clustering
I used TFIDF and an NMF model to create topic clusters.  Note that the colors do not have any specific meaning.  They were just meant to highlight topics of interest.
![alt text](/images/termiteplots.png)
Clinton spent a lot of time on the campaign trail targeting minority groups.  She spoke to many African American communities, women’s organizations and veterans, which you can see highlighted here. Trump’s topics are less defined but we can see some topics on the economy and national defense.

With a little more filtering Clinton’s topic change slightly, but are still clearly defined.  The topics are less clear for Trump. Immigration jumps out, but the other topics tend to fall apart.  This may be an indication of why the Trump campaign wouldn’t publish the actual transcripts.
![alt text](/images/termiteplots2.png)



### Twitter Bots
Based on the campaign speeches and debate transcripts, I created a Twitter bot for both Clinton and Trump.  The vocabulary for each candidate was constructed from the collected the collected speech and debate transcripts .

The tweet generation model uses the Markov model where the following word is based on the preceding trigram.

Clinton's dictionary consists of 142,523 unique trigrams.
Trump's dictionary consists of 149,892 unique trigrams.


I then collected hashtags from Clinton's and Trump's historical tweets using Twitter's REST API.  I collected the most commonly used hashtags from each candidate and then randomly added one, two or none to the generated tweet.


 I started the debate by tweeting the other candidate online and then the bots tweeted back and forth to each other every 3 minutes.   Each tweet was stored in an SQL database and when that database was updated, the corresponding bot knew to tweet back and used the words from the most recent tweet as the input for the response tweet.

I then decided to do a social experiment. From the data collected in part 1, I randomly selected a user to tag.  My initial goal was to see how many followers I could obtain in the remaining week.  Unfortunately after I started going this, I was quickly suspended from using Twitter's API.


![alt text](/images/twitterwar.png)


https://twitter.com/KillaryHilton_
https://twitter.com/TonaldDrump___


## Part 3

### The Data
The textacy library has a corpus that contains over 11,000 congressional speeches (1996-2016) from 13 different congress people involved in the 2016 election. The congress people recommendations are limited to the following people:


| Republicans   |Democrats      | Independents |
| ------------- |:-------------:| -----:|
| Marco Rubio   | Bernie Sanders | Jim Webb |
| Ted Cruz    | Barack Obama     |    |
| Rand Paul | Hillary Clinton      |   |
| Mike Pence | Joe Biden    |     |
| Lindsey Graham |Lincoln Chafee   |    |
| John Kasich |       |     |
| Rick Santorum |      |     |   |

The model uses TFIDF and a Naive Bayes model to find the probability that specific keywords are from a particular party or candidate.  The model only focuses on nouns, verbs and adjectives.  I hope to add a sentiment component in the future.  

Example output:
![alt text](/images/website.png)


The web app was created through Flask and can be accessed at:  www.discovercongress.co
