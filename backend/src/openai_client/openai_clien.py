from openai import OpenAI
import json
from typing import Optional, Dict

class OpenAIClient:
    def __init__(self, api_key: str = None):
        self.client = OpenAI(api_key=api_key)

    def describe_image(self, image_url: str, post_title: str, prompt: str) -> Optional[str]:
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt + post_title},
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
        except Exception as e:
            print(f'Failed OpenAI request: {e}')
            print(f'Post title: {post_title}, Image URL: {image_url}')
            return None

    def parse_response(self, response_string: str) -> Dict[str, str]:
        try:
            # Extract the JSON part from the input string
            json_part = response_string.strip('```python\n').strip('```')
            data = json.loads(json_part)
            return {
                "alternate_title": data["alternate_title"],
                "gre_word": data["gre_word"]
            }
        except json.JSONDecodeError as e:
            print(f'Failed to parse response: {e}')
            return {"alternate_title": "", "gre_word": ""}