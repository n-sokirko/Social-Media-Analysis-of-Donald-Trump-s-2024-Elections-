# collect_users.py

def collect_user_list(reddit, subreddits, keywords, user_limit=100):
    user_list = set()
    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        print(f': {subreddit_name}')
      
        for submission in subreddit.search(' OR '.join(keywords), limit=100):
            if submission.author:
                user_list.add(submission.author.name)
            submission.comments.replace_more(limit=0)
            for comment in submission.comments:
                if comment.author:
                    user_list.add(comment.author.name)
            if len(user_list) >= user_limit:
                break
        if len(user_list) >= user_limit:
            break
    return list(user_list)
