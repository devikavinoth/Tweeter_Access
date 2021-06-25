
import tweepy as tw
import sqlalchemy

if __name__ == '__main__':
	#Inputs
    print("Accessing both Twitter application and Json")
    consumer_key = "cd8iGcrNYdg6wbqFUzguu1VSU"
    consumer_secret = "bOW6XQoSPrtJb1zvDUMajbmrOf3lx5zjqwzJz65DdCls51Rrmn"
    access_token = "1407673852566532098-Lg8rs51w4S5naXiIMXXzfYkK9yVGwI"
    access_token_secret = "aayR5WyZUAAA5BwHV2NxYBYU2CHANLxMZ5hzvKlUSTJ4f"

    # Authenticate to Twitter
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tw.API(auth)
    #verify the authendication
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    timeline = api.home_timeline()
    for tweet in timeline:
        print(tweet.created_at,tweet.text)
    print(sqlalchemy.__version__)
