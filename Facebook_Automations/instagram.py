from datetime import timedelta
from datetime import datetime
# from analytics.analyticsrecorder import MeasurementName,Constants,TagsName,FieldName,AnalyticsRecord
# from django.utils import timezone
import requests
# import logging
# import urllib2

# ar =  AnalyticsRecord()

class Constant():
    api_base_url = "https://graph.facebook.com"
    auth_code_url = api_base_url+"/oauth/authorize/"
    access_token_url = api_base_url+"/oauth/access_token"
    feed_connection = "/feed"
    ACCESS_TOKEN = "EAAFToPQuPTEBAJyUY5raasQW0s0nnaZA16ZCvIPKyovbhFYOLbEQ1zTor3MeiOnZAPQfBGu4ayKLWOnZA1KiBxRjZAOtOg5Fhu1ZBkfZAr8JNthNLD66aAHXzLGmvfisk2nTMZAx5OCbEWjeaIbS9XDCY6KCdXq7KENzBh1MMiohjWR82f6BNG08rvmv8JokUs0yDbWpDNPZAeAZDZD"
    user_id = "/me"
    version = "/v3.2"
    client_id = "808fb92577244e6292a2b536147f19ce"
    client_secret = "c630a4c3997a4eecb6d75cdf3eef09d8"
    grant_type = "authorization_code"
    redirect_uri = "http://localhost"
    code = "code"
    access_token="access_token"
    response_type = code
    read_media_api = "https://api.instagram.com/v1/users/self/media/recent/?access_token=11568692993.808fb92.74d1f9342f994241901688f66b73bce0"
    FB_PAGE_ID = '/373122386749686'
    INSTA_BUSINESS_ACCOUNT_ID="/xxxxxxxxxxx"
    MEDIA_OBJECT_CONTAINER_ENDPOINT = "/media"
    PUBLISH_MEDIA_OBJECT_ENDPOINT = '/media_publish'
class Helper():
    def __init__(self):
        pass

class Instagram(object):

    def __init__(self):
        pass

    def create_media_object_container(self):

        try:
            url =  Constant.api_base_url+Constant.version+Constant.INSTA_BUSINESS_ACCOUNT_ID+Constant.MEDIA_OBJECT_CONTAINER_ENDPOINT
            print url
            data = {"media_url": "image url", "caption":"Image title and description"}
            response = requests.post(url, data=data)
            print response.text
            # ar.write_social_media_api_calls("instagram","media_object_container", "success", 1)
            return response.text['creation_id']
        except Exception as e:
            print e
            # ar.write_social_media_api_calls("instagram","media_object_container", "failure", 0)


    def publish_media_container_to_instagram(self, creation_id):
        url =  Constant.api_base_url+Constant.version+Constant.INSTA_BUSINESS_ACCOUNT_ID+Constant.PUBLISH_MEDIA_OBJECT_ENDPOINT
        print url
        data = {"creation_id": creation_id}
        response = requests.post(url, data=data)
        print response.text
        # ar.write_social_media_api_calls("instagram","media_publish", "success", 1)
        return

    def get_instagram_business_account_details(self):
        try:
            # 373122386749686?fields=instagram_business_account
            parameters = {'access_token': Constant.ACCESS_TOKEN, 'fields':"instagram_business_account"}
            url =  Constant.api_base_url+Constant.version+str(Constant.FB_PAGE_ID)
            print(url)
            response = requests.post(url, params=parameters)
            print response.json()
            # ar.write_social_media_api_calls("instagram","business_account_id", "success", 1)

        except Exception as e:
            print(e)
            # ar.write_social_media_api_calls("instagram","business_account_id", "failure", 0)     



    def instagram(self):
        try:
            # if ar.get_number_of_insta_api_calls_in_last_hour()<198:
                # self.get_auth_code()
            creation_id =  self.create_media_object_container()
            self.publish_media_container_to_instagram(creation_id)

        except Exception as e:
            logging.getLogger("cinfo_log").exception("Exception in facebook automation")


Instagram().instagram()

#****Output of above scripts*****

'''https://graph.facebook.com/v3.2/xxxxxxxxxxx/media
{"error":{"message":"(#803) Cannot query users by their username (xxxxxxxxxxx)","type":"OAuthException","code":803,"fbtrace_id":"FeQWJLdCCbf"}}
string indices must be integers
https://graph.facebook.com/v3.2/xxxxxxxxxxx/media_publish
{"error":{"message":"(#803) Cannot query users by their username (xxxxxxxxxxx)","type":"OAuthException","code":803,"fbtrace_id":"Ap2PHeECBJi"}}
'''

