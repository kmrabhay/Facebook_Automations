from rest_framework.renderers import JSONRenderer
from ott.models import OttGroup, OttMessage
from datetime import timedelta
from datetime import datetime
from analytics.analyticsrecorder import MeasurementName,Constants,TagsName,FieldName,AnalyticsRecord
from django.utils import timezone
from mongoengine.queryset.visitor import Q
import requests
import logging
import urllib2

class Constant():
    api_base_url = "https://graph.facebook.com"
    auth_code_url = api_base_url+"/oauth/authorize/"
    access_token_url = api_base_url+"/oauth/access_token"
    feed_connection = "/feed"
    ACCESS_TOKEN = "EAAjZBJa4A31YBAKSnwJJCD55SLsgZBKUjUzEIqvA3z2VMLiReA9wAdazrFbCmFZBNZB5OBxZB91X833fZCPnUZA80fx4S3cmrGlORji6hu5aaPzEAiKkLZCZCfZA4V85ZBEZCPeCHMD8mBXurBcOQJgNd1VnybUhSxw5JcFQuyZAJx1W8yAZDZD"
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
    INSTA_BUSINESS_ACCOUNT_ID="/17841409597243611"
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
            data = {"image_url": 'http://img.multiplymyleads.com/images/logo_mml.jpg', "caption":"Image title and description"}
            response = requests.post(url, data=data)
            print response
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
        print response
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


# Instagram().instagram()

#****Output of above scripts*****

'''
(venv) abhay@Abhay:~/mml/mml-dev$ python manage.py instagram_postings
https://graph.facebook.com/v3.2/17841409597243611/media
<Response [400]>
{"error":{"message":"Unsupported post request. Object with ID '17841409597243611' does not exist, cannot be loaded due to missing permissions, or does not support this operation. Please read the Graph API documentation at https:\/\/developers.facebook.com\/docs\/graph-api","type":"GraphMethodException","code":100,"error_subcode":33,"fbtrace_id":"Bd6lNOxF+hS"}}
string indices must be integers
https://graph.facebook.com/v3.2/17841409597243611/media_publish
<Response [400]>
{"error":{"message":"(#100) The parameter creation_id is required.","type":"OAuthException","code":100,"fbtrace_id":"Axsiz6WnJGV"}}


'''
