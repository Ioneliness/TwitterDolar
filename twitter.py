import tweepy

auth = tweepy.OAuthHandler('wFUfO43LN12zobfD8sVz4IpG4', 'a9ehGavnVMceRLpV5LDv39PjmtKj1W2MwEbUtyT818m0v7wwJy')
auth.set_access_token('1299813553881395200-rSHyUEiMfbLeHtlO6fjOGYzDact9MT', 'JVBPXaVCrvNxvzORLM7bpnDztLezyrlO0s0FjmWQu6485')

api = tweepy.API(auth,  wait_on_rate_limit=True)