# Define custome class for posts data
from datetime import datetime as dt

class Post:
    def __init__(self, title, vocab, user, description = None, photo = None, time_posted = dt.now()):
        self.post_title = title
        self.post_photo = photo
        self.time_posted = time_posted
        self.vocab = vocab
        self.post_description = description
        self.post_user = user

    @staticmethod
    def from_dict(source):
        # [START_EXCLUDE]
        post = Post(source["post_title"], source["vocab"], source["user"])

        if "selftext" in source:
            post.post_description = source["selftext"]

        if "url" in source:
            post.post_photo = source["url"]

        if "time_posted" in source:
            post.time_posted = source["time_posted"]

        return post
        # [END_EXCLUDE]

    def to_dict(self):
        # [START_EXCLUDE]
        dest = {"post_title": self.post_title, "vocab": self.vocab, "post_user": self.post_user}

        if self.post_description:
            dest["post_description"] = self.post_description

        if self.post_photo:
            dest["post_photo"] = self.post_photo

        if self.time_posted:
            dest["time_posted"] = self.time_posted

        return dest
        # [END_EXCLUDE]

    def __repr__(self):
        return f"Post(\
                title={self.post_title}, \
                vocab={self.vocab}, \
                user={self.post_user}, \
                description={self.post_description}, \
                photo={self.post_photo}, \
                time={self.time_posted}\
            )"
