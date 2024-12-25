# visualize_data.py

import plotly.express as px

def plot_activity_over_time(df):
    daily_counts = df.groupby(['day', 'type']).size().reset_index(name='counts')
    fig = px.line(
        daily_counts,
        x='day',
        y='counts',
        color='type',
        title='Activity Over Time'
    )
    fig.show()

def plot_user_popularity(df, top_users):
    top_users_data = df[df['username'].isin(top_users)]
    fig = px.line(
        top_users_data,
        x='date',
        y='score',
        color='username',
        title='User Popularity Over Time'
    )
    fig.show()
