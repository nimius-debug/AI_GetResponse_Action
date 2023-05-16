import openai
import datetime
import random
import os
from helperGR import upload_image_to_getresponse
# from GetResponse import *
from base64 import b64decode
from datetime import datetime
import pytz

try:
    OPEN_AI = os.environ['OPEN_AI']
    openai.api_key = OPEN_AI
    model_id = 'gpt-3.5-turbo'
    AI_key_message = "Open AI key was accepted!"
except KeyError:
    OPEN_AI = "OPEN_AI Token not available!"
    AI_key_message = "GetResponse key was not avaialble!"


IMAGE_SAVE_FOLDER = "img"
STYLE_LIST = [
    "Impressionism Monet",
    "Cubism Picasso",
    "Street art graffiti",
    "3D",
    "Low poly",
    "Digital painting",
    "Memphis ,bold, kitch, colourful, shapes"
]

def get_practical(book_title):
    AI_practical_personality = "You're a helpful assistant that writes practical tips for emails base on books."
    response = openai.ChatCompletion.create(
        model = model_id,
        messages = [
            {"role": "system", "content": AI_practical_personality },
            {"role": "user", "content": f"Write one practical idea from the {book_title}'s book that you could start applying today in 50 words or less \
                                        dont go on details, be practical, funny , and inspirational to convey the most important practical takeaway.\
                                        Focus on using simple, easy-to-understand and concise language. "},
        ],
        temperature = 1.0,
        max_tokens = 120
    )
    return response.choices[0].message.content

def get_summary( book_title):
    AI_summary_personality = "You're a storytelling assistant that summarizes books with a humorous, friendly, and conversational tone,\
                        engaging readers interested in launching online businesses or side hustles for passive income."
    response = openai.ChatCompletion.create(
        model = model_id,
        messages = [
            {"role": "system", "content": AI_summary_personality },
            {"role": "user", "content": f"the goal is to provide a brief summary of '{book_title}' in 80 words or less that will pique \
                                        someone's interest and encourage them to read the book for themselves.\
                                        Use story telling, funny and inspirational tone to convey the most important takeaways. Focus on using simple, easy-to-understand language.\
                                        Try to be as concise as possible, while still conveying the essence of the book."},
        ],
        temperature = 1.0,
        max_tokens = 150
    )


    return response.choices[0].message.content

def get_subject( book_title):
    AI_subject_personality = "You're a helpful assistant that writes subject line questions for emails base on the book title  ."
    response = openai.ChatCompletion.create(
        model = model_id,
        messages = [
            {"role": "system", "content": AI_subject_personality },
            {"role": "user", "content": f"write an a subject line based on '{book_title}' book. Make sure is provocative and makes \
                                        the recipient eger to click on it. \
                                        Remember, the goal is to make them take action and click on the email. "},
        ],
        temperature = 1.0,
    )
    return response.choices[0].message.content

def get_subject_img(book_title):
    AI_practical_personality = "You're a helpful assistant that writes practical tips for emails base on books."
    response = openai.ChatCompletion.create(
        model = model_id,
        messages = [
            {"role": "system", "content": AI_practical_personality },
            {"role": "user", "content": f"can you create an prompt to capture an image related to '{book_title}' 15 word max.\
                                        Only output the prompt dont include the book in your response or the word prompt.\
                                        '''example 1 \
                                        Book: The 4-Hour Workweek \
                                        Prompt: a family in vacation in the beach'''\
                                        '''example 2 \
                                        Book: The War of Art \
                                        Prompt: a chinese person figthing '''\
                                        '''example 3 \
                                        Book: Meditations \
                                        Prompt: a women doing yoga in the outside'''\
                                        '''example 4 \
                                        Book: High Growth Handbook \
                                        Prompt: a person studying in a building'''\
                                        example 5 \
                                        Book: Steve Jobs \
                                        Prompt: a men inovating with a phone''' \
                                        '''example 6 \
                                        Book: The Outsiders\
                                        Prompt: A group of teenagers hanging out near a deserted lot'''\
                                        '''example 7 \
                                        Book: 1984\
                                        Prompt: a person looking fearful in front of a large screen'''\
                                        '''example 8 \
                                        Book: The Alchemist\
                                        Prompt: a person crossing the desert with a camel'''\
                                        '''example 9 \
                                        Book: The Fountainhead\
                                        Prompt: A city skyline with a prominent skyscraper'''\
                                        '''example 10 \
                                        Book: Animal Farm\
                                        Prompt: A group of farm animals standing on their hind legs in protest'''\
                                        " 
                                        
            },
        ],
        temperature = 1.0,
        max_tokens = 20
    )
    return response.choices[0].message.content


def get_image(subject, book_title):
    random_style = random.choice(STYLE_LIST)
    try:
        response = openai.Image.create(
            prompt=f"{random_style} of {subject}",
            n=1,
            size="256x256",
            response_format="b64_json",
        )
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return None


    image_name = f"{book_title}_{response['created']}.png"
    image_data = response["data"][0]["b64_json"]
    img_url = save_image(image_data, image_name)
    return img_url

def save_image(image_data, image_name):
    decoded_image_data = b64decode(image_data)
    image_path = os.path.join(IMAGE_SAVE_FOLDER, image_name)
    with open(image_path, mode="wb") as png:
        png.write(decoded_image_data)
    img_url = upload_image_to_getresponse(image_path, image_name)
    return img_url    
    
def get_schedule():
    # Define the timezone
    tz = pytz.timezone('America/New_York')
    # Get current date in the defined timezone
    now = datetime.now(tz)
    # Set time to 12:30 PM
    now = now.replace(hour=12, minute=30, second=0, microsecond=0)
    # Format the datetime in ISO 8601
    ISO8601_date_string = now.isoformat()
    print(f"Schedule date: {ISO8601_date_string}")
    return ISO8601_date_string
