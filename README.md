# Reddit Bitcoin Sentiment Analysis

## Overview

This Python script retrieves posts from the Bitcoin subreddit using the Reddit API and analyzes the sentiment of each post's title and body text using NLTK's VADER sentiment analyzer. It then calculates the percentage of positive, negative, and neutral posts.

## Prerequisites

- Python 3.11
- `dotenv` Python package
- `praw` Python package
- `nltk` Python package

## Setup

1. Clone the repository or download the source code.
2. Install the required packages by running:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a virtual environment by running:
   ```bash
   python -m venv .venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source .venv/bin/activate
     ```
5. Create a `.env` file in the root directory and provide your Reddit API credentials:
   ```plaintext
   CLIENT_ID="your_client_id"
   CLIENT_SECRET="your_client_secret"
   USER_AGENT="your_user_agent"
   ```
6. Optionally, you can use the provided `.env.example` file as a template.

## Usage

1. Run the script by executing:
   ```bash
   python main.py
   ```
2. The script will fetch posts from the Bitcoin subreddit and analyze their sentiment.
3. The results will be displayed, showing the total number of posts analyzed and the percentage of positive, negative, and neutral posts.

## Example

```bash
Total posts analyzed: 100
Positive posts: 60.00%
Negative posts: 20.00%
Neutral posts: 20.00%
```

## License

This project is licensed under the [MIT License](LICENSE).

---
