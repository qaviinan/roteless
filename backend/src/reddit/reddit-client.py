import praw
import config
import json

def is_image_url(url):
    """
    Check if the URL points to an image based on its extension.
    
    :param url: The URL to check.
    :return: True if the URL is an image, False otherwise.
    """
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp')
    return url.lower().endswith(image_extensions)

class RedditClient:
    def __init__(self) -> None:
        self.client = praw.Reddit(
            client_id="w_Q28DYmr9LyTwOBFDyn-A",
            client_secret="cZc5Pl_l0K9DCIPOkWGrlI-Dmrsiqg",
            user_agent="web:genfeed:v0.1.0 (by /u/bisonGRE)",
            timeout=45
            )
        print("CONNECTED TO REDDIT:", self.client.read_only)
        self.subreddits = config.SUBLIST
        self.submission_methods = config.SUBMISSION_METHODS 

    def get_posts(self, num_posts, subreddit):
        print('Trying to get_posts() for sub:', subreddit)
        greentext = self.client.subreddit(subreddit).hot(limit=num_posts)
        trylist = greentext
        idx = 0
        all_posts = []
        for submission in trylist:
            # title
            is_sticky = getattr(submission, 'stickied', None)
            if is_sticky:
                continue
            else:
                is_image = is_image_url(getattr(submission, "url", None))
                if is_image:
                    post_items = {}
                    for attribute_name in self.submission_methods:
                        # Safely get attribute with a default value if not found
                        attribute_value = getattr(submission, attribute_name, None)
                        post_items[attribute_name] = attribute_value
                    all_posts.append(post_items)
                    idx += 1  # Ensure idx is incremented inside the loop
        return all_posts
    
    def loop_subreddits(self, subreddits = None, num_subs = 10):
        sublist = subreddits if subreddits else self.subreddits
        pass