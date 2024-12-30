import os
from utils.post import Post
from reddit_client import RedditClient
from openai_client import OpenAIClient
from firebase_handler import FirebaseHandler
import config

def main():
    # Initialize the required clients and handlers
    reddit_client = RedditClient(config.REDDIT_CREDENTIALS)
    openai_client = OpenAIClient(config.OPENAI_API_KEY)
    firebase_handler = FirebaseHandler(config.FIREBASE_CONFIG)

    # Step 1: Scrape posts from chosen subreddits
    print("Scraping posts from subreddits...")
    posts_data = reddit_client.scrape_posts(
        subreddits=config.SUBREDDITS,
        limit=config.POST_LIMIT
    )

    # Convert scraped data into Post objects
    posts = [Post(data) for data in posts_data]

    # Step 2: Process posts in bulk through OpenAI to generate captions
    print("Generating captions using OpenAI...")
    for i in range(0, len(posts), config.BATCH_SIZE):
        batch = posts[i:i + config.BATCH_SIZE]

        # Collect image URLs for this batch
        image_urls = [post.image_url for post in batch if post.image_url]

        # Generate captions for the batch
        captions = openai_client.generate_captions(image_urls)

        # Attach captions back to the Post objects
        for post, caption in zip(batch, captions):
            post.caption = caption

    # Step 3: Save posts to Firebase in bulk
    print("Saving posts to Firebase...")
    firebase_handler.save_posts_in_bulk(posts)

    print("Process completed successfully!")

if __name__ == "__main__":
    main()
