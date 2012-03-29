# -*- coding: UTF-8 -*-

class AbuseMiddleware(object):

    def process_request(self, request):
        print "I am a request"

    def process_response(self, request, response):
        print "I am a response"
        return response
