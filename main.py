import tweepy

# 先ほど取得した各種キーを代入する
CK = os.environ.get("ACCESS_TOKEN")
CS = os.environ.get("ACCESS_TOKEN_SECRET")
AT = os.environ.get("API_KEY")
AS = os.environ.get("API_SECRET_KEY")



# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

api = tweepy.API(auth)

# 1ツイートずつループ
for status in api.search(q='@matatabi_math', count=50):
    tweet_id = status.id
    # 例外処理をする
    try:
        # リツイート実行
        api.retweet(tweet_id)
    except:
        print('error')
