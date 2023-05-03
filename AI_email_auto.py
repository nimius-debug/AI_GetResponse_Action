import openai
import amz_books
import random
import os

amazon_books = amz_books.amz_book
# print(amazon_books)
# Replace with your OpenAI API key
try:
    OPEN_AI = os.environ['OPEN_AI']
    openai.api_key = OPEN_AI
    model_id = 'gpt-3.5-turbo'
    AI_key_message = "Open AI key was accepted!"
except KeyError:
    OPEN_AI = "OPEN_AI Token not available!"
    AI_key_message = "GetResponse key was not avaialble!"

def get_practical(book_title):
    AI_practical_personality = "You're a helpful assistant that writes practical tips for emails base on books."
    response = openai.ChatCompletion.create(
        model = model_id,
        messages = [
            {"role": "system", "content": AI_practical_personality },
            {"role": "user", "content": f"What is one practical idea from the {book_title}'s book that you could start applying today?\
                                        How could this idea help you to learn more and improve your skills? \
                                        Write a brief paragraph explaining the idea and how you could implement it in your life in 50 words or less.\
                                        Try to use simple, easy-to-understand vocabulary and be as specific as possible. \
                                        Remember, the goal is to take action and apply what you've learned from the book to your own life. "},
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
            {"role": "user", "content": f"Can you briefly summarize the key ideas of '{book_title}' in 80 words or less?\
                                        Imagine you're explaining the book to someone who has never read it before.\
                                        Focus on the most important takeaways, using simple, easy-to-understand language.\
                                        What are the key themes or concepts that the author explores?\
                                        What are the main arguments or ideas that the author presents?\
                                        Try to be as concise as possible, while still conveying the essence of the book.\
                                        Remember, the goal is to provide a brief summary that will pique \
                                        someone's interest and encourage them to read the book for themselves."},
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


def get_image(subject):
    style = ["Impressionism Monet", 
            "Cubism Picasso",
            "Street art graffiti",
            "Isometric 3D",
            "Low poly",
            "Digital painting",
            "Memphis ,bold, kitch, colourful, shapes",
            "realistic picture"
            ]
    random_style = random.choice(style)
    response = openai.Image.create(
        prompt = f"{random_style} of {subject}",
        n=1,
        size="256x256"
    )
    return response['data'][0]['url']

book_title = random.choice(list(amazon_books.keys()))
print(book_title)
book_link = amazon_books[book_title]
# img_subject = get_subject_img(book_title)
# print(img_subject)
# print(get_image(img_subject, book_title))
# summary = get_summary(AI_summary_personality,book_title)
# subject = get_subject(AI_subject_personality,book_title)
# practical_use = get_practical(AI_practical_personality,book_title)

def html_tamplate(book_title, subject, img_link, summary, practical_use, book_link ):
    html_email = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>{book_title}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                font-size: 16px;
                line-height: 1.5;
                text-align: center;
                margin: 0;
                padding: 0;
                width: 100%;
                -webkit-text-size-adjust: 100%;
                -ms-text-size-adjust: 100%;
            }}
            h1 {{
                font-size: 24px;
                margin-top: 30px;
                margin-bottom: 20px;
            }}
            .container p {{
                margin-bottom: 50px;
                font-size:16px;
                line-height: 2.2;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                padding-top:5px;
                padding-bottom:30px;
                padding-right:30px;
                padding-left:30px;
                background-color: #f7f7f7;
                border-style: outset;
                border-radius: 5px;
                border-width:3px;
                line-height: 1.5;
                
            }}
            .button {{
                margin-top:20px;
                margin-left:20px;
                display: inline-block;
                padding: 10px 20px;
                font-size: 18px;
                color: #fffff6;
                background-color: #333;
                border-radius: 4px;
                border-color:red;
                text-decoration: none;
            }}
            .signature {{
                font-family: cursive;
                font-size: 1rem;
                line-height: 1;
            }}
            .bottom {{
                background-color: #333;
                color: #fff;
                padding: 20px;
                font-size: 14px;
            }}
            .hover-link {{
                color: #FFF; 
                font-weight: normal;
                text-decoration: none;
            }}
            .hover-link:hover {{
                color: #708238; 
                text-decoration: underline; 
            }}
            li{{
                color:#0B6623;
                font-size:18px;
            }}
        </style>
    </head>
    <body>
        <table width="100%" border="0" cellspacing="0" cellpadding="0">
            <tr>
                <td align="center">
                    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="max-width: 600px; margin: 0 auto;">
                        <tr>
                            <td>
                                <div class="container">
                                    <h1>{subject}</h1>
                                    <a href={book_link}>
                                        <img src={img_link} alt={book_title}  >
                                    </a>
                                    <p>{summary}</p>
                                    <div class="container">
                                        <h3>Real One</h3>
                                        <li>{practical_use}</li>
                                    </div>
                                    <span>
                                        <strong>More Real Ones >>>>> </strong>
                                    </span>
                                    <a href={book_link} class="button">
                                        <strong class="hover-link">Read me!</strong>
                                    </a>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td class="bottom">
                                <p class="signature">Jorge A. Gil</p>
                                <p>&copy; 2023 JAG LLC. All rights reserved.</p>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """
    return html_email

def plain_text_tamplate(subject, img_link,summary, practical_use, book_link):
    plain_text_email = f"""{subject} {img_link} {summary} Real One: {practical_use} More Real Ones >>>>>{book_link} Read me!"""
    
    return plain_text_email

