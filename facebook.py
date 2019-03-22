from rest_framework.renderers import JSONRenderer
from ott.models import OttGroup, OttMessage
from datetime import timedelta
from datetime import datetime
from analytics.analyticsrecorder import MeasurementName,Constants,TagsName,FieldName,AnalyticsRecord
from django.utils import timezone
from mongoengine.queryset.visitor import Q
import requests
import logging
ar =  AnalyticsRecord()

class Constant():
    api_base_url = "https://graph.facebook.com"
    feed_connection = "/feed"
    ACCESS_TOKEN = "ACCESS_TOKEN FOUND USING GRAPH API EXPLORE"
    photos_connection = "/photos"
    list_of_groups="/groups"
    user_id = "/me"
    test_group_id = "/414283372663330"
    version = "/v3.2"

class Helper():
    def __init__(self):
        pass
    def process_read_feed_api_result(self, result):
        try:
            print "Total post: ", len(result['data'])
            for post in result['data']:
                message_date = post['updated_time']
                message =  post['message']
                post_id = post['id']
                channel =  4
                print post_id
                post_link = Constant.api_base_url+"/"+str(post_id)
                om =  OttMessage(message=message, message_date=message_date, \
                        channel=channel, post_link=post_link)
                om.save()
                print "Created OttEntry"
        except Exception as e:
            print(e)

    def process_group_list_api_result(self, result):
        try:
            for group in result['data']:
                og = OttGroup(group_name=group['name'], group_id=group['id'])
                og.save()
        except Exception as e:
            print(e)


class Facebook(object):

    def __init__(self):
        pass

    def get_list_of_groups(self, user_id):
        try:
            group_list_url = Constant.api_base_url+Constant.version+user_id+Constant.list_of_groups
            print(group_list_url)
            parameters = {'access_token': Constant.ACCESS_TOKEN}      
            response = requests.get(group_list_url, params=parameters)
            print response.json()
            ar.write_social_media_api_calls("facebook","group_list", "success", 1)
            if response.json():
                Helper().process_read_feed_api_result(response.json())

            return response.json()
        except Exception as e:
            print(e)
            ar.write_social_media_api_calls("facebook","group_list", "failure", 0)            
    def read_group_feed(self, group_id):

        try:
            parameters = {'access_token': Constant.ACCESS_TOKEN}
            group_url =  Constant.api_base_url+Constant.version+str(group_id)+Constant.feed_connection
            print(group_url)
            response = requests.get(group_url, params=parameters)
            print response.json()
            total_feed_read =  len(response.json()['data'])
            ar.write_social_media_api_calls("facebook","read_feed", "success", total_feed_read)
            if response.json():
                Helper().process_read_feed_api_result(response.json())

            return response.json()
        except Exception as e:
            print(e)
            ar.write_social_media_api_calls("facebook","read_feed", "failure", 0)
    def post_to_group(self, group_id, message):

        try:
            data = {'access_token': Constant.ACCESS_TOKEN, "message": message}
            group_url =  Constant.api_base_url+Constant.version+str(group_id)+Constant.feed_connection
            print(group_url)
            response = requests.post(group_url, data=data)
            print response.text
            ar.write_social_media_api_calls("facebook","post_feed", "success", 1)
            return response.text
        except Exception as e:
            print(e)
            ar.write_social_media_api_calls("facebook","post_feed", "failure", 0)       

    def post_image_posting_to_facebook(self, group_id):

        try:
            upload_photo_url = Constant.api_base_url+Constant.version+group_id+Constant.photos_connection
            import os
            # image = open('me.jpg','rb').read()
            # print image

            files = {
                'file': open('me.jpg', 'rb'),
                'file': open('Abhay.jpg', 'rb'),
                'media': open('me.jpg', 'rb'),
                  
            }
            # files = [('file', open('me.jpg', 'rb')), ('file', open('Abhay.jpg', 'rb'))]

            data = {'access_token': Constant.ACCESS_TOKEN, "message": "This is test photos"}
            print upload_photo_url

          

            response = requests.post(upload_photo_url, data=data, files=files)
            print response.text
            ar.write_social_media_api_calls("facebook","post_feed", "success", 1)
            return response.text

        except Exception as e:
            print(e)
    def facebook(self):

        try:
            if ar.get_number_of_fb_api_calls_in_last_hour()<198:
                self.post_image_posting_to_facebook(Constant.test_group_id)
                # self.read_group_feed(Constant.test_group_id)
                # self.post_to_group(Constant.test_group_id, "Required 2bhk in hyderabad")
                # self.get_list_of_groups(Constant.user_id)
                # i+=1
        except Exception as e:
            logging.getLogger("cinfo_log").exception("Exception in facebook automation")
