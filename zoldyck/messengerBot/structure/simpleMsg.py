import json


class simpleMsg():
    def __init__(self):
        self.type = "simple"

    def createTextMsgJson(self, rec_ID, msg, msg_type, tag=None,
                          notification_type="REGULAR"):
        """This functions responsible for creating Json Object
           to send text message to facebook messenger

        Arguments:
            rec_ID {string}   -- recipient id
            msg {string}      -- message you want to send to messenger
            msg_type {string} -- identifies the messaging type of the message being sent
            https://developers.facebook.com/docs/messenger-platform/send-messages#messaging_types

        Keyword Arguments:
            tag {string}      -- Message tags give you the ability to send messages to 
                                 a person outside of the normally allowed 24-hour window
                                 for all possible values check link] (default: {None})
            https://developers.facebook.com/docs/messenger-platform/send-messages/message-tags

            notification_type {str} -- Push notification type (default: {"REGULAR"})
            https://developers.facebook.com/docs/messenger-platform/reference/send-api/#payload

        Returns:
            Json Object -- complete Json Object to be send to facebook API
        """
        json_body = dict()
        if msg_type == "MESSAGE_TAG":
            json_body["tag"] = tag
        json_body["messaging_type"] = msg_type
        json_body["recipient"] = {"id": rec_ID}
        json_body["message"] = {"text": msg}
        json_body["notification_type"] = notification_type
        json_body = json.dumps(json_body)
        return json_body

    def createMediaByURLJson(self, url, rec_ID, media_type, Assest=False):
        """This functions responsible for creating Json Object
           to send message with attachment (image,video,audio,files)
           to facebook messenger by URL

        Arguments:
            url {string} -- URL of the media you want to send
            rec_ID {string} -- recipient id
            media_type {string} -- type of medial (image,video,audio,files)

        Keyword Arguments:
            Assest {bool} -- [check if you want to save this attachment in facebook
                              if it is true facebook will send you id for this attach.] (default: {False})

        Returns:
            Json Object -- complete Json Object to be send to facebook API
        """
        json_body = dict()
        json_body["recipient"] = {"id": rec_ID}
        json_body["message"] = {"attachment": {"type": media_type, "payload":
                                {"url": url, "is_reusable": str(Assest).lower()
                                 }}}
        json_body = json.dumps(json_body)
        return json_body

    def createMediaByAssestIdJson(self, rec_ID, media_type, assestID):
        """This functions responsible for creating Json Object
           to send message with attachment (image,video,audio,files)
           to facebook messenger by Assest ID
           for more info : https://developers.facebook.com/docs/messenger-platform/send-messages/saving-assets

        Arguments:
            rec_ID {string} -- recipient id
            media_type {string} -- type of medial (image,video,audio,files)
            assestID {string} -- id given by facbook when you save attachment in it

        Returns:
            Json Object -- complete Json Object to be send to facebook API
        """
        json_body = dict()
        json_body["recipient"] = {"id": rec_ID}
        json_body["message"] = {"message": {"attachment": {"type": media_type,
                                "payload": {"attachment_id": assestID}}}}
        json_body = json.dumps(json_body)
        return json_body

    def creatTypingStatusJson(self, rec_ID, status):
        """This functions responsible for creating Json Object
           to create (seen , typing on , typing off) effect in
           facebook messenger

        Arguments:
            rec_ID {string} -- recipient id
            status {string} -- status of the boot (seen , typing on , typing off)

        Returns:
            Json Object -- complete Json Object to be send to facebook API
        """
        json_body = dict()
        json_body["recipient"] = {"id": rec_ID}
        if status == "on":
            json_body["sender_action"] = "typing_on"
        elif status == "off":
            json_body["sender_action"] = "typing_off"
        elif status == "seen":
            json_body["sender_action"] = "mark_seen"
        json_body = json.dumps(json_body)
        return json_body
