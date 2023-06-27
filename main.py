from GetResponse import *
from AI_email_auto import *
from Html_plain_templates import *
import logging
import logging.handlers
import amz_books
import os

BOOK_TRACKER_FILE = 'book_tracker.txt'

def load_book_tracker():
    if not os.path.exists(BOOK_TRACKER_FILE):
        return set()
    
    with open(BOOK_TRACKER_FILE, 'r') as file:
        book_tracker = set(file.read().splitlines())
        
    return book_tracker

def save_book_tracker(book_tracker):
    with open(BOOK_TRACKER_FILE, 'w') as file:
        for book_title in book_tracker:
            file.write(book_title + '\n')
            
def main():
    book_tracker = load_book_tracker()
    amazon_books = amz_books.amz_book
    remaining_books = set(amazon_books.keys()) - book_tracker
    
    if not remaining_books:
        # All books have been sent, reset the book tracker
        book_tracker.clear()
    
    book_title = random.choice(list(remaining_books))
    book_tracker.add(book_title)
    book_link = amazon_books[book_title]
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger_file_handler = logging.handlers.RotatingFileHandler(
        "status.log",
        maxBytes=1024 * 1024,
        backupCount=1,
        encoding="utf8",
    )
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logger_file_handler.setFormatter(formatter)
    logger.addHandler(logger_file_handler)
    
    logger.info(f"Token value: {GR_key_message}")
    logger.info(f"Token value: {AI_key_message}")
    
    get_response = GetResponseAPI(book_title)
    #get from_fields and preprocces data
    from_fields = get_response.get_from_fields()
    preprocess_from_fields = get_response.preprocessing_from_fields(from_fields)
    # print(preprocess_from_fields)
    from_field_id = preprocess_from_fields[0]['id']
    #print(from_field_id)
    
    # #get campaigns and preprocces data
    # campaigns = get_response.get_campaigns()
    # preprocesses_campaigns = get_response.preprocessing_campaigns_info(campaigns)
    # print(preprocesses_campaigns)
    # campaign_id = preprocesses_campaigns[0]['id']
    # print(campaign_id)
    AI_book_recomendation_less3 = "MLUJj"
    AIBOOK_more3 = "MFjPB"
    testing_campaign_id = "M5A2G"
    # AI part get the book data 
    subject = get_subject(book_title)
    
    summary = get_summary(book_title)
    sentences_split = summary.split(". ")
    # Add the period back to each sentence
    summary_sentences_split = [s + "." for s in sentences_split]

    practical_use = get_practical(book_title)
    practical_use_split = practical_use.split(". ")
    practical_use_split = [s + "." for s in practical_use_split]
    
    #image generator
    AI_img_subject = get_subject_img(book_title)
    AI_img = get_image(AI_img_subject, book_title)
    print(AI_img)
    
    # get schedule time
    schedule_time = get_schedule()
    
    # send email                       book_title,subject, img_link, summary, practical_use
    body_html = simple_html_tamplate( book_title ,subject, AI_img, summary_sentences_split, practical_use_split)
    body_plain = simple_plain_text_tamplate(book_title, subject, AI_img, sentences_split, practical_use_split)
    get_response.send_email_to_campaign_contacts(AI_book_recomendation_less3,schedule_time, subject, body_html,body_plain, from_field_id)
    get_response.send_email_to_campaign_contacts(AIBOOK_more3,schedule_time, subject, body_html,body_plain, from_field_id)
    # logging the status
    logger.info(f"message send succesfully from : {preprocess_from_fields[0]} to {AI_book_recomendation_less3} and {AIBOOK_more3} subject: {subject} book: {book_title}")
    logging.info('\n')
    save_book_tracker(book_tracker)

if __name__ == '__main__':
    main()