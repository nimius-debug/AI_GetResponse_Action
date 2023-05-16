import requests
import json
import random
import os

try:
    GET_RESPONSE = os.environ["GET_RESPONSE"]
    GR_key_message = "GetResponse key was accepted!"
except KeyError:
    GET_RESPONSE = "GetResponse key not available!"
    GR_key_message = "GetResponse key was not accepted!"


class GetResponseAPI:
    def __init__(self, book_title):
        self.headers = {
            'Content-Type': 'application/json',
            'X-Auth-Token': f'api-key {GET_RESPONSE}'
        }
        self.campaign_name = f'{book_title}_AI_book' + str(random.randint(1,1000))
        
    #*-***************************from-fields***************************-#
    def get_from_fields(self):
        url = 'https://api.getresponse.com/v3/from-fields'
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return json.loads(response.text)
        except requests.exceptions.RequestException as e:
            print(f'Error getting from fields: {e}')
            return None
        except json.JSONDecodeError as e:
            print(f'Error decoding JSON response: {e}')
            return None

    def preprocessing_from_fields(self, from_fields):
        return [{
            'name': from_user['name'],
            'id': from_user['fromFieldId'],
            'email': from_user['email']
        } for from_user in from_fields]
    
    #*-***************************campaigns***************************-#
    def get_campaigns(self):
        url = 'https://api.getresponse.com/v3/campaigns'
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return json.loads(response.text)
        except requests.exceptions.RequestException as e:
            print(f'Error getting from fields: {e}')
            return None
        except json.JSONDecodeError as e:
            print(f'Error decoding JSON response: {e}')
            return None

    def get_contacts_count_in_campaign(self, campaign_id):
        contacts_count = 0
        per_page = 1000
        page = 1

        while True:
            contacts_url = f'https://api.getresponse.com/v3/contacts?query[campaignId]={campaign_id}&perPage={per_page}&page={page}'
            contacts_response = requests.get(contacts_url, headers=self.headers)
            contacts = json.loads(contacts_response.text)

            contacts_count += len(contacts)

            if len(contacts) < per_page:
                break

            page += 1

        return contacts_count

    def preprocessing_campaigns_info(self, campaigns):
        preprocessed_campaigns = [{
            'name': campaign['name'],
            'id': campaign['campaignId'],
            'contacts_count': self.get_contacts_count_in_campaign(campaign['campaignId'])
        } for campaign in campaigns]

        sorted_campaigns = sorted(preprocessed_campaigns, key=lambda x: x['contacts_count'], reverse=True)

        return sorted_campaigns

    #*-***************************send email to contacts***************************-#
    def send_email_to_campaign_contacts(self, campaign_id,schedule_time, subject, body_html, body_plain, from_field_id):
        message = {
            "content": {
                "html": body_html,
                "plain": body_plain
            },
            "flags": [
                "openrate"
            ],
            "name": self.campaign_name,
            "type": "broadcast",
            "editor": "custom",
            "subject": subject,
            "fromField": {
                "fromFieldId": from_field_id
            },
            
            "replyTo": {
                "fromFieldId": from_field_id
            },
            "campaign": {
                "campaignId": campaign_id
            },
            "sendOn": schedule_time,
            "sendSettings": {
                "selectedCampaigns": [campaign_id],
                "selectedSegments": [],
                "selectedSuppressions": [],
                "excludedCampaigns": [],
                "excludedSegments": [],
                "selectedContacts": [],
                "timeTravel": "false",
                "perfectTiming": "false",
            }
        }

        url = 'https://api.getresponse.com/v3/newsletters'
        response = requests.post(url, headers=self.headers, json=message)

        if response.status_code == 201:
            print(f'Successfully sent email to all contacts in campaign (ID: {campaign_id})')
        else:
            error_message = response.text
            print("status code: ",response.status_code)
            try:
                error_json = json.loads(response.text)
                
                if error_json['httpStatus'] == 400 and error_json['code'] == 1000:
                    context = error_json['context']
                    for c in context:
                        error_message += f"\nError in {c['validationType']}, field {c['fieldName']}: {c['errorDescription']}"
                elif error_json['httpStatus'] == 401 and error_json['code'] == 1014:
                    error_message += "\nUnable to authenticate request. Check credentials or authentication method details"
                elif error_json['httpStatus'] == 404 and error_json['code'] == 1013:
                    error_message += "\nThe requested resource was not found"
                elif error_json['httpStatus'] == 429 and error_json['code'] == 1015:
                    context = error_json['context']
                    error_message += f"\nToo many requests to API, quota reached, please wait until next quota window. Current limit: {context['currentLimit']}, Time to reset: {context['timeToReset']}"
            except:
                pass
            
            print(f'Error sending email to campaign (ID: {campaign_id}): {error_message} {response.status_code}')
                
          
    