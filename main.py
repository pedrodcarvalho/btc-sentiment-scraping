import os
from dotenv import load_dotenv
import praw
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def main():
    # Reddit API credentials
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    USER_AGENT = os.getenv('USER_AGENT')

    # Authenticate with Reddit API
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent=USER_AGENT)

    # Search for posts in a subreddit
    subreddit = reddit.subreddit('bitcoin')
    posts = subreddit.search('Bitcoin', limit=None)

    # Initialize sentiment analyzer
    sid = SentimentIntensityAnalyzer()

    # Analyze sentiment of each post
    positive_count = 0
    negative_count = 0
    neutral_count = 0

    for post in posts:
        # Extract title and body of the post
        text = f'{post.title} {post.selftext}'

        # Analyze sentiment
        ss = sid.polarity_scores(text)

        # Classify sentiment
        if ss['compound'] > 0.05:
            positive_count += 1
        elif ss['compound'] < -0.05:
            negative_count += 1
        else:
            neutral_count += 1

    # Calculate percentages
    total_posts = positive_count + negative_count + neutral_count
    positive_percentage = (positive_count / total_posts) * 100
    negative_percentage = (negative_count / total_posts) * 100
    neutral_percentage = (neutral_count / total_posts) * 100

    # Display results
    print(f'Total posts analyzed: {total_posts}')
    print(f'Positive posts: {positive_percentage:.2f}%')
    print(f'Negative posts: {negative_percentage:.2f}%')
    print(f'Neutral posts: {neutral_percentage:.2f}%')


if __name__ == '__main__':
    load_dotenv()
    main()
