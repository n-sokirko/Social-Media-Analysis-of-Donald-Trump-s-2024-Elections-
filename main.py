# main.py

import os
from config import init_reddit
from collect_users import collect_user_list
from collect_activity import collect_user_activity
from process_data import save_data_to_json, load_data_from_json, convert_data_to_dataframe
from visualize_data import plot_activity_over_time, plot_user_popularity

def main():
    # Parameters
    subreddits = ['politics', 'Conservative', 'Trump']
    keywords = ['Trump 2024', 'Donald Trump', 'elections 2024']
    user_limit = 100
    data_filename = 'reddit_trump2024_data.json'

    # Check if data file exists
    if os.path.exists(data_filename):
        print(f'Data file "{data_filename}" found. Loading data from file.')
        # Load data from the existing file
        user_data = load_data_from_json(data_filename)
    else:
        print(f'Data file "{data_filename}" not found. Collecting data from Reddit.')
        # Initialize Reddit API
        reddit = init_reddit()
        
        # Collect the list of users
        user_list = collect_user_list(reddit, subreddits, keywords, user_limit)
        print(f'Collected {len(user_list)} users.')

        # Collect user activity
        user_data = collect_user_activity(reddit, user_list, keywords)
        print(f'Collected {len(user_data)} records.')

        # Save data
        save_data_to_json(user_data, data_filename)
        print(f'Data saved to "{data_filename}".')

    # Process data
    df = convert_data_to_dataframe(user_data)

    # Visualize data
    plot_activity_over_time(df)

    # Analyze user popularity
    top_users = df.groupby('username')['score'].sum().nlargest(5).index
    plot_user_popularity(df, top_users)

if __name__ == '__main__':
    main()
