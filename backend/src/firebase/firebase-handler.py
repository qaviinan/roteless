from post import Post

class firebase_handler:
    def __init__(self, db) -> None:
        self.db = db
    
    def check_duplicates(self, all_posts):
        posts_ref = self.db.collection('posts')
        existing_ids = set()
        # Collect post IDs to check in batch
        post_ids = [post['id'] for post in all_posts]

        # Using a batch query to check for existing posts
        batch_size = 10
        for i in range(0, len(post_ids), batch_size):
            batch_ids = post_ids[i:i + batch_size]
            docs = posts_ref.where('post_id', 'in', batch_ids).stream()
            for doc in docs:
                existing_ids.add(doc.to_dict()['post_id'])
        return existing_ids
    
    def add_post(self, mypost):
        # mypost = Post(title, vocab, user, description, photo).to_dict()
        update_time, post_ref = self.db.collection("posts").add(mypost)
        print(f"At time {update_time} Added document with id {post_ref.id}")
    # TODO
    # 1. parse gpt-response to separate gre_word and alternate_title
    # 2. Add post.from_dict(post) to below function
    # 3. Once done, delete existing posts from firestore and upload batch as test
    # 4. After testing, migrate to aws lambda function

    def add_posts(self, posts):
        # Maximum batch size for Firestore is 500 writes per batch
        batch_size = 500
        batches = []
        current_batch = self.db.batch()
        counter = 0

        for post in posts:
            mypost = Post.from_dict(post)
            post_ref = self.db.collection('posts').document(post['id'])
            current_batch.set(post_ref, mypost.to_dict())
            counter += 1

            if counter == batch_size:
                batches.append(current_batch)
                current_batch = db.batch()
                counter = 0

        if counter > 0:
            batches.append(current_batch)

        for batch in batches:
            batch.commit()

        print(f"{len(posts)} posts added to Firestore in {len(batches)} batches.")