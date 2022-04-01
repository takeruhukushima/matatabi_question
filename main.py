import tweepy
import os

# # 先ほど取得した各種キーを代入する
# CK = "L4YkZDGRcD7mKgv5vfRrjohYO"
# CS = "buQLqU0o2aG5RwhDjtHJwJBtr4Jq5X7ky4IelMgWWnVFKfJ4HL"
# AT = "1468856376126763009-Zm7yHauW6WoxjDEpFu0pya8Pyk0CUZ"
# AS = "PPtdqnPJEdp1AOAiFZEoxONtVQjnSIn7uPq3vxQE37TSj"

CK=os.environ.get("CK")
CS=os.environ.get("CS")
AT=os.environ.get("AT")
AS=os.environ.get("AS")


# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

api = tweepy.API(auth)

# 1ツイートずつループ
for status in api.search(q='#またたび質問箱数学', count=50):
    tweet_id = status.id
    # 例外処理をする
    try:
        # リツイート実行
        api.retweet(tweet_id)
    except:
        print('error')
