from GetResponse import *
from AI_email_auto import *
import logging
import logging.handlers

def main():
    
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
    
    get_response = GetResponseAPI()
    #get from_fields and preprocces data
    from_fields = get_response.get_from_fields()
    preprocess_from_fields = get_response.preprocessing_from_fields(from_fields)
    #print(preprocess_from_fields[0])
    from_field_id = preprocess_from_fields[0]['id']
    #print(from_field_id)
    
    #get campaigns and preprocces data
    campaigns = get_response.get_campaigns()
    preprocesses_campaigns = get_response.preprocessing_campaigns_info(campaigns)
    #print(preprocesses_campaigns[0])
    campaign_id = preprocesses_campaigns[0]['id']
    #print(campaign_id)
    
    # AI part get the book data 
    subject = get_subject(book_title)
    summary = get_summary(book_title)
    practical_use = get_practical(book_title)
    #image generator
    AI_img_subject = get_subject_img(book_title)
    AI_img = get_image(AI_img_subject)
    # send email
    body_html = html_tamplate(book_title, subject, AI_img, summary, practical_use, book_link)
    body_plain = plain_text_tamplate(subject, AI_img, summary, practical_use, book_link)
    get_response.send_email_to_campaign_contacts(campaign_id, subject, body_html,body_plain, from_field_id)
    # logging the status
    logger.info(f"message send succesfully from : {preprocess_from_fields[0]} to {preprocesses_campaigns[0]} subject: {subject} book: {book_title}")
    
    # for campaign_info in preprocesses_campaigns:
    #     print(f'Campaign "{campaign_info["name"]}" (ID: {campaign_info["id"]}): {campaign_info["contacts_count"]} contacts')

if __name__ == '__main__':
    main()