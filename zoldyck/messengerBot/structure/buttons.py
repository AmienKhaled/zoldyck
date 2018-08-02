import json


class buttons():
    
    def createUrlButtonJson(self, url, title, webHeightRatio="full"):
        """Create button when you press it it open url
        
        Arguments:
            url {string} -- url of site you whant to go to when button pressed
            title {string} -- title of button
        
        Keyword Arguments:
            webHeightRatio {str} -- Height of the Webview (default: {"full"})
        
        Returns:
            Json Object -- json object of button
        """

        json_body = {"type": "web_url", "url": url, "title": title,
                     "webview_height_ratio": webHeightRatio}
        json_body = json.dumps(json_body)
        return json_body

    def createUrlButtonWithMsgExtJson(self, url, title, fullbackIRL,
                                      webHeightRatio="full",
                                      messengerExt="false"):
        """Create button when you press it it open url with messenger Extention
        
        Arguments:
            url {string} -- url of site you whant to go to when button pressed
            title {string} -- title of button
            fullbackIRL {[type]} -- The URL to use on clients that don't support Messenger Extensions.
                                    If this is not defined, the url will be used as the fallback.
                                    It may only be specified if messenger_extensions is true.

        Keyword Arguments:
            webHeightRatio {str} -- Height of the Webview (default: {"full"})
            messengerExt {str} -- Must be true if using Messenger Extensions. (default: {"false"})
        
        Returns:
            Json Object -- json object of button
        """

        json_body = {"type": "web_url", "url": url, "title": title,
                     "webview_height_ratio": webHeightRatio}
        json_body["messenger_extensions"] = "true"
        json_body["fallback_url"] = fullbackIRL
        json_body = json.dumps(json_body)
        return json_body

    def createPostbackButtonJson(self, title, payload):
        """Create button when you press it send request to ypur server with text -payload-
        
        Arguments:
            title {string} -- title of button
            payload {string} -- text you want to be send to your server
        
        Returns:
            Json Object -- json object of button
        """

        json_body = {"type": "postback", "title": title, "payload": payload}
        json_body = json.dumps(json_body)
        return json_body

    def createShareButtonJson(self, title, subtitle, imageUrl,
                              tempUrl, Urlbutton=[]):
        """[summary]

        Arguments:
            title {string} -- title of button
            subtitle {string} -- subtitle of the temp
            imageUrl {string} -- url of photo to the template
            tempUrl {string} -- url you want user go to when template is pressed

        Keyword Arguments:
            Urlbutton {list} -- list of buttons to share it (default: {[]})

        Returns:
            Json Object -- json object of button
        """

        json_body = {"type": "element_share",
                     "share_contents": {"attachment": {"type": "template", "payload": {"template_type": "generic",
                                                                                       "elements": [{"title": title,
                                                                                                     "subtitle": subtitle,
                                                                                                     "image_url": imageUrl,
                                                                                                     "default_action": {
                                                                                                         "type": "web_url",
                                                                                                         "url": tempUrl},
                                                                                                     "buttons": Urlbutton}]}}}}
        json_body = json.dumps(json_body)
        return json_body

    def createPriceListJson(self, label, amount):
        """create list of prices to be added to buy button
        
        Arguments:
            label {string} -- label of price
            amount {string} -- amount of the product
        
        Returns:
            Json Object -- json object of button
        """

        json_body = {"label": label, "amount": amount}
        json_body = json.dumps(json_body)
        return json_body


    def createBuyButtonJson(self, title, payload, currency, payment_type,
                            Pricelists, merchant_name, is_test_payment="true"):
        """[summary]
        
        Arguments:
            title {string} -- title of button
            payload {string} -- Developer defined metadata about the purchase.
            currency {string} -- Currency for price.
            payment_type {string} -- Must be FIXED_AMOUNT or FLEXIBLE_AMOUNT.
            Pricelists {list} -- List of objects used to calculate total price.
                                 Each label is rendered as a line item in the checkout dialog.
            merchant_name {string} -- Name of merchant.
        
        Keyword Arguments:
            is_test_payment {str} -- Optional. Whether this is a test payment. Once set to true, the charge will be a dummy charge.
        
        Returns:
            Json Object -- json object of button
        """

        json_body = {"type": "payment", "title": title, "payload": payload}
        json_body["payment_summary"] = {"currency": currency, "payment_type": payment_type,
                                        "is_test_payment": is_test_payment, "merchant_name": merchant_name}
        json_body["payment_summary"]["requested_user_info"] = ["shipping_address", "contact_name", "contact_phone",
                                                               "contact_email"]
        json_body["payment_summary"]["price_list"] = {"price_list": Pricelists}
        json_body = json.dumps(json_body)
        return json_body

    def createCallButton(self, title, phoneNumber):
        """[summary]
        
        Arguments:
            title {string} -- title of button
            phoneNumber {string} -- Format must have "+" prefix followed by the country code,
                                    area code and local number. For example, +16505551234.
        
        Returns:
            Json Object -- json object of button
        """

        json_body = {"type": "phone_number", "title": title,
                     "payload": phoneNumber}
        json_body = json.dumps(json_body)
        return json_body
