from reddit import RedditClient
import config
from openai import OpenAI
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore
from firebase import firebase_handler
import json
import time
load_dotenv()
client = OpenAI()

# Step 0: Load the reddit posts (preferably as a separate process)
# Step 1: For each image post:
#           1. Get image description from 40
#           2. Send (image, title, rag_wordlist) = gre_caption
#           3. append (gre_caption, image, url) to finished_posts
#           4. Turn finished posts into html and save for viewing

def describe_image(image_url, post_title, type='describe'):
    # Just asking for what's in the image
    if type=='describe':
        prompt = config.image_prompt+post_title
    else:
        prompt = config.full_prompt + post_title
    
    try:
        response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                "type": "image_url",
                "image_url": {
                    "url": image_url,
                    "detail": "low"
                },
                },
            ],
            }
        ],
        max_tokens=300,
        )
        return response.choices[0].message.content
    except:
        print('Failed openai request')
        print(post_title, image_url)
    


def save_dict_list_to_json(dict_list, json_file='oneshot_temp_posts.json'):
    with open(json_file, 'w') as file:
        json.dump(dict_list, file, indent=4)
    print(f"JSON file '{json_file}' created/updated successfully.")

def parse_string(input_string):
    # Extract the JSON part from the input string
    json_part = input_string.strip('```python\n').strip('```')
    
    # Parse the JSON string to a dictionary
    data = json.loads(json_part)
    
    # Create a dictionary with the required key-value pairs
    result = {
        "alternate_title": data["alternate_title"],
        "gre_word": data["gre_word"]
    }
    return result

def single_step_captions(all_posts):
    for post in all_posts:
        gre_caption_string = describe_image(image_url=post['thumbnail'], post_title=post['title'], type='single-step')
        parsed_caption = parse_string(gre_caption_string)
        post['post_title'] = parsed_caption['alternate_title']
        post['vocab'] = parsed_caption['gre_word']
        post['user'] = 'dankbot'
    return all_posts

def run(numsubs=2):
    reddit_client = RedditClient()
    cred = credentials.Certificate("roteless-vgtppm-firebase.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    firebase = firebase_handler(db)
    sublist = config.SUBLIST[:numsubs]
    
    for sub in sublist:
        all_posts = reddit_client.get_posts(10, sub)
        # Some post IDs already exist in Firebase
        existing_ids = firebase.check_duplicates(all_posts)
        new_posts = [post for post in all_posts if post['id'] not in existing_ids]
        if new_posts:
            oneshot_done_posts = single_step_captions(new_posts)
            firebase.add_posts(oneshot_done_posts)
            save_dict_list_to_json(oneshot_done_posts, f"{sub}_temp_posts.json")
            print(f'SAVED altered posts for sub:{sub}')

# image_url = all_posts[1]['thumbnail']
# post_title = all_posts[1]['title']
# rag_wordlist = ['hyperbole', 'doggerel', 'apothegm', 'lampoon', 'fatuous']

def timed_run():
    start_time = time.time()
    
    reddit_client = RedditClient()
    print(f"Initialized Reddit client in {time.time() - start_time:.2f} seconds")
    
    start_time = time.time()
    cred = credentials.Certificate("roteless-vgtppm-firebase.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    firebase = firebase_handler(db)
    print(f"Initialized Firebase in {time.time() - start_time:.2f} seconds")
    
    start_time = time.time()
    sublist = config.SUBLIST
    print(f"Loaded subreddit list in {time.time() - start_time:.2f} seconds")
    
    for sub in sublist:
        section_start_time = time.time()
        all_posts = reddit_client.get_posts(100, sub)
        print(f"Fetched posts from {sub} in {time.time() - section_start_time:.2f} seconds")
        
        section_start_time = time.time()
        existing_ids = firebase.check_duplicates(all_posts)
        new_posts = [post for post in all_posts if post['id'] not in existing_ids]
        print(f"Checked duplicates and filtered new posts in {time.time() - section_start_time:.2f} seconds")
        
        if new_posts:
            section_start_time = time.time()
            oneshot_done_posts = single_step_captions(new_posts)
            print(f"Processed new posts in {time.time() - section_start_time:.2f} seconds")
            
            section_start_time = time.time()
            firebase.add_posts(oneshot_done_posts)
            print(f"Added posts to Firebase in {time.time() - section_start_time:.2f} seconds")
            
            section_start_time = time.time()
            save_dict_list_to_json(oneshot_done_posts, f"./tempfiles/{sub}_temp_posts.json")
            print(f"Saved posts to JSON in {time.time() - section_start_time:.2f} seconds")
            
            print(f"SAVED altered posts for sub:{sub}")

    total_time = time.time() - start_time
    print(f"Total run time: {total_time:.2f} seconds")

if __name__=="__main__":
    timed_run()