

class jsonHandler():

    def checkForMessageAttr(self, receivedJson):
        """check for message attribute inside the json
        
        Arguments:
            receivedJson {json} -- received json
        
        Returns:
            bool -- if it is inside the json or not
        """

        result = receivedJson["entry"][0]["messaging"][0].get("message", "no")
        if result == "no":
            return False
        return True

    def checkForAttachment(self, receivedJson):
        """check for Attachment attribute inside the json
        
        Arguments:
            receivedJson {json} -- received json
        
        Returns:
            bool -- if it is inside the json or not
        """

        result = receivedJson["entry"][0]["messaging"][0].get("message").get("attachments", "no")
        if result == "no":
            return False
        return True

    def checkForQuickReply(self, receivedJson):
        """check for Quick Reply attribute inside the json
        
        Arguments:
            receivedJson {json} -- received json
        
        Returns:
            bool -- if it is inside the json or not
        """

        result = receivedJson["entry"][0]["messaging"][0].get("message").get("quick_reply", "no")
        if result == "no":
            return False
        return True

    def checkForText(self, receivedJson):
        """check for Text attribute inside the json
        
        Arguments:
            receivedJson {json} -- received json
        
        Returns:
            bool -- if it is inside the json or not
        """

        result = receivedJson["entry"][0]["messaging"][0].get("message").get("text")
        if result == "no":
            return False
        return True

    def checkForPostback(self, receivedJson):
        """check for Postback attribute inside the json
        
        Arguments:
            receivedJson {json} -- received json
        
        Returns:
            bool -- if it is inside the json or not
        """
        result = receivedJson["entry"][0]["messaging"][0].get("postback", "no")
        if result == "no":
            return False
        return True

    def returnJsonType(self, receivedJson):
        """it detect the type of message sent
        
        Arguments:
            receivedJson {json} -- received json
        
        Returns:
            string -- type of the message
        """

        if not self.checkForMessageAttr(receivedJson):
            if self.checkForPostback(receivedJson):
                return "postback"

        if self.checkForAttachment(receivedJson):
            return receivedJson["entry"][0]["messaging"][0].get("message").get("attachments")[0].get("type")

        elif self.checkForQuickReply(receivedJson):
            return "quick_reply"

        elif self.checkForText(receivedJson):
            return "text"

    def getQuickReplyPayload(self, receivedJson):
        """get the quick reply payload from received json
        
        Arguments:
            receivedJson {json} -- received json
        
        Returns:
            string -- payload of false in there is no quick reply payload
        """

        if not self.checkForQuickReply(receivedJson):
            return "False"
        return receivedJson["entry"][0]["messaging"][0].get("message").get("quick_reply").get("payload")

    def getAttachementLink(self, receivedJson):
        """get the attachment link from received json
        
        Arguments:
            receivedJson {json} -- received json
        
        Returns:
            string -- Attachement Link
        """

        if not self.checkForAttachment(receivedJson):
            return "False"
        return receivedJson["entry"][0]["messaging"][0].get("message").get("attachments")[0].get("payload").get("url")

    def returnReceptionId(self, receivedJson):
        """get the user -sender- id
        
        Arguments:
            receivedJson {json} -- received json
        
        Returns:
            string -- user -sender- id
        """

        return receivedJson["entry"][0]["messaging"][0]["sender"]["id"]

    def returnReceivedText(self, receivedJson):
        """it the type of received message is text, so this function bet you that text
        
        Arguments:
            receivedJson {json} -- received json
        
        Returns:
            string -- received text
        """

        text = receivedJson["entry"][0]["messaging"][0].get("message")
        if text:
            return text["text"]

    def returnPostbackPayload(self, receivedJson):
        """get the postback text received
        
        Arguments:
            receivedJson {json} -- received json
        
        Returns:
             string -- received postback
        """

        return receivedJson["entry"][0]["messaging"][0].get("postback")["payload"]

    def returnPostbackTitle(self, receivedJson):
        """get the postback title received
        
        Arguments:
            receivedJson {json} -- received json
        
        Returns:
             string -- received postback title
        """

        return receivedJson["entry"][0]["messaging"][0].get("postback")["title"]

    def returnLatAndLong(self, receivedJson):
        """get the latitude and longitude received from location quick reply
        
        Arguments:
            receivedJson {json} -- received json
        
        Returns:
             json -- latitude and longitude
        """

        return receivedJson["entry"][0]["messaging"][0].get("message").get("attachments")[0].get("payload").get("coordinates")

