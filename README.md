# AI Book Recommendation GetResponse_Action

AI Book Recommendation GetResponse_Action
AI Book Recommendation GetResponse_Action is a Python-based application that utilizes OpenAI's GPT-3.5 model to generate a book subject, summary, practical application, and an image(Dall-e). The generated content is then sent to a GetResponse email campaign using the GetResponse API.
Automated using GithubActions

## Requirements
* Python 3.8 or higher
* openai==0.27.6
* requests==2.29.0

## Installation
 
1. Clone this repository:

2. Navigate to the cloned directory:

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4.Set up your GetResponse API Key and OpenAI API Key in the ```environment```
```bash
GET_RESPONSE=your_getresponse_api_key
OPEN_AI=your_openai_api_key
```
5. Run the main script:
```bash
python main.py
```

## Config
in the amz_book.py add and change the existing books to the ones you like 

## License

[MIT](https://choosealicense.com/licenses/mit/)

