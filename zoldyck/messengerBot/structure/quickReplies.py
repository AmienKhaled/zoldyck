import json


class quickReplies():

    def creatTextQuickReplyJson(self, title, payload, buttonImageUrl):
        """create text reply which user can press it inside messenger

        Arguments:
            title {string} -- [name appear on reply]
            payload {string} -- text defined by programmer which will be
                                return to server if user press the reply
            buttonImageUrl {string} -- URL for png photo for reply

        Returns:
            Json Object -- only return json for text reply
        """

        json_body = dict()
        json_body = {"content_type": "text", "title": title,
                     "payload": payload, "image_url": buttonImageUrl}
        json_body = json.dumps(json_body)
        return json_body

    def creatLocationQuickReplyJson(self):
        """create reply which user can press it inside messenger
           it will open a map allowing user to choose location
           then messenger will send back to server latitude and longitude

        Returns:
            Json Object -- only return json for location reply
        """

        json_body = dict()
        json_body = {"content_type": "location"}
        json_body = json.dumps(json_body)
        return json_body

    def creatPhoneNumberQuickReplyJson(self, payload, buttonImageUrl):
        """create reply which user can press it inside messenger
           to send his phone number

        Arguments:
            payload {string} -- text defined by programmer which will be
                                return to server if user press the reply
            buttonImageUrl {string} -- URL for png photo for reply

        Returns:
            Json Object -- only return json for number reply
        """

        json_body = dict()
        json_body = {"content_type": "user_phone_number", "payload": payload,
                     "image_url": buttonImageUrl}
        json_body = json.dumps(json_body)
        return json_body

    def creatEmailQuickReplyJson(self, payload, buttonImageUrl):
        """create reply which user can press it inside messenger
           to send his email

        Arguments:
            payload {string} -- text defined by programmer which will be
                                return to server if user press the reply
            buttonImageUrl {string} -- URL for png photo for reply

        Returns:
            Json Object -- only return json for email reply
        """

        json_body = dict()
        json_body = {"content_type": "user_email", "payload": payload,
                     "image_url": buttonImageUrl}
        json_body = json.dumps(json_body)
        return json_body


    def creatFullRepliesWithTextJson(self, rec_ID, text, repliesArray):
        """create full json to send all replies you have created
           to facebook messenger with simple text above it

        Arguments:
            rec_ID {string} -- recipient id
            text {string} -- text will be sent above replies
            repliesArray {list} -- list of replies json

        Returns:
            Json Object -- complete Json Object to be send to facebook API
        """

        json_body = dict()
        json_body["recipient"] = {"id": rec_ID}
        json_body["message"] = {"text": text, "quick_replies": repliesArray}
        json_body = json.dumps(json_body)
        return json_body

    def creatFullRepliesWithMediaJson(self, rec_ID, repliesArray, mediaType,
                                      content, contentTypeAssest=False):
        """create full json to send all replies you have created
           to facebook messenger with attachment above it

        Arguments:
            rec_ID {string} -- recipient id
            repliesArray {list} -- list of replies json
            mediaType {string} -- type of medial (image,video,audio,files)
            content {string} -- url or Assest id of attachment

        Keyword Arguments:
            contentTypeAssest {bool} -- if true that means (content) argument
                                        is Assest Id not URL (default: {False})

        Returns:
            Json Object -- complete Json Object to be send to facebook API
        """

        json_body = dict()
        json_body["recipient"] = {"id": rec_ID}
        json_body["message"] = {"quick_replies": repliesArray}
        if (contentTypeAssest is False):
            json_body["message"]["attachment"] = {"type": mediaType, "payload":
                                                  {"url": content}}
        else:
            json_body["message"]["attachment"] = {"type": mediaType, "payload":
                                                  {"attachment_id": content}}
        json_body = json.dumps(json_body)
        return json_body
