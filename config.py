SUBLIST = ["wholesomememes", "memes", "blursedimages", "WhitePeopleTwitter", 
"tumblr", "hellsomememes", "dankmemes","clevercomebacks", "meme", "dank_meme",
"Animemes", "HistoryMemes", "MemeAlleway", "greentext"]

SUBMISSION_METHODS = ['id', 'url', 'thumbnail', 'view_count', 'ups', 'upvote_ratio','stickied', 'title', 'selftext', 'media', 'media_embed', 'link_flair_text', 'is_video']
# 'over_18', 'preview/images'

full_prompt = """
I will give you a meme image and an associated title.
You will write an alternate title for each meme as a regular person who is sharing this on their social media. 
But the catch is that every caption must have a gre word in it.
Here are the rules of writing your caption;
1. Captions can be as short as just 1 word (provided that word is a gre word). 
2. Write them using a witty, observational humor tone.
3. Write your response as a python dict with three items as follows;
    {"original_title" : "here-goes-original-title",
    "alternate_title" : "here-goes-alternate-title-with-gre-word",
    "gre_word" : "the-gre-word-used-in-the-alternate-title"}
    
Example of response;
    {"original_title" : "Bro has too many demands",
    "alternate_title" : "Bro is too exacting",
    "gre_word" : "exacting"}

Here is the image and title;
"""

image_prompt = "I'm giving you an image of a meme and its title. You'll tell me what's in the image with a focus on the meaning conveyed. Here's the title;"

rag_prompt = """
I will give you a meme image and an associated title.
You will write an alternate title for each meme as a regular person who is sharing this on their social media. 
But the catch is that every caption must have a gre word in it. Here are the rules of writing your caption;
1. Captions can be as short as just 1 word (provided that word is a gre word). 
2. Write them using a witty, observational humor tone.
3. ONLY respond with the caption itself and no other text
4. Example of proper response: "Fatuous Financial Advice"

Now, here is the post title:{title}
Description of the image:{image}
Here is a list of suggested GRE words for this caption: {suggested_words}, you may use them or use another GRE word, depending on suitability.
"""