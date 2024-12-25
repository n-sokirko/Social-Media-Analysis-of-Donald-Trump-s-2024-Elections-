# collect_activity.py

import time
import logging
from prawcore.exceptions import Forbidden, NotFound, PrawcoreException

def collect_user_activity(reddit, user_list, keywords):
    user_data = []
    for username in user_list:
        try:
            user = reddit.redditor(username)
            # Collect comments
            for comment in user.comments.new(limit=100):
                if any(keyword.lower() in comment.body.lower() for keyword in keywords):
                    user_data.append({
                        'username': username,
                        'type': 'comment',
                        'content': comment.body,
                        'score': comment.score,
                        'created_utc': comment.created_utc
                    })
            # Collect submissions
            for submission in user.submissions.new(limit=50):
                if any(keyword.lower() in submission.title.lower() for keyword in keywords):
                    user_data.append({
                        'username': username,
                        'type': 'submission',
                        'content': submission.title + ' ' + submission.selftext,
                        'score': submission.score,
                        'created_utc': submission.created_utc
                    })
            # Add a delay to respect API rate limits
            time.sleep(1)
        except Forbidden:
            logging.warning(f'Forbidden error when accessing user {username}. Skipping.')
        except NotFound:
            logging.warning(f'User {username} not found. Skipping.')
        except PrawcoreException as e:
            logging.warning(f'PRAW error for user {username}: {e}')
        except Exception as e:
            logging.error(f'Unexpected error processing user {username}: {e}')
    return user_data
