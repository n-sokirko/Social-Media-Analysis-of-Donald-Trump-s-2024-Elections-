# config.py

import praw


CLIENT_ID = 'H4dKeaNVrUZuGIPeZnGC8w'
CLIENT_SECRET = 'PBp_SchwVnCjAuE5EjtyenCDDsJbjg'
USER_AGENT = 'python:Mikita Sakirko:1.0 (by /u/BowlCreepy2601)'

def init_reddit():
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT
    )
    return reddit
