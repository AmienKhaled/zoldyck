import json


class templates(): 

    def createDefaultActionJson(self, url, webHeightRatio="full"):
        """The default action executed when the template is tapped.
        
        Arguments:
            url {string} -- url of site you whant to go to when it pressed
        
        Keyword Arguments:
            webHeightRatio {string} -- Height of the Webview (default: {"full"})
        
        Returns:
            Json Object -- json object of Default Action section
        """

        json_body = {"type": "web_url", "url": url,
                     "webview_height_ratio": webHeightRatio}
        json_body = json.dumps(json_body)
        return json_body

    def createDefaultActionWithMsgExtJson(self, url, fullbackIRL,
                                          webHeightRatio="full"):
        """The default action executed when the template is tapped.
           with messenger Extention
        
        Arguments:
            url {string} -- url of site you whant to go to when button pressed
            fullbackIRL {string} -- The URL to use on clients that don't support Messenger Extensions.
                                    If this is not defined, the url will be used as the fallback.
                                    It may only be specified if messenger_extensions is true.
        
        Keyword Arguments:
            webHeightRatio {string} -- Height of the Webview (default: {"full"})
        
        Returns:
            Json Object -- json object of Default Action section
        """

        json_body = {"type": "web_url", "url": url,
                     "webview_height_ratio": webHeightRatio}
        json_body["messenger_extensions"] = "true"
        json_body["fallback_url"] = fullbackIRL
        json_body = json.dumps(json_body)
        return json_body

    def createElementJson(self, title, subTitle, imageUrl, defaultAction):
        """body of the template
        
        Arguments:
            title {string} -- The title to display in the template. 80 character limit.
            subTitle {string} -- The subtitle to display in the template. 80 character limit.
            imageUrl {string} -- The URL of the image to display in the template.
            defaultAction {json} -- The default action executed when the template is tapped.
        
        Returns:
            Json Object -- json object of element section
        """

        json_body = {"title": title, "image_url": imageUrl,
                     "subtitle": subTitle, "default_action": defaultAction}
        json_body = json.dumps(json_body)
        return json_body

    def createElementWithButtonJson(self, title, subTitle, imageUrl,
                                    defaultAction, buttons):
        """body of the template with button
        
        Arguments:
            title {string} -- The title to display in the template. 80 character limit.
            subTitle {string} -- The subtitle to display in the template. 80 character limit.
            imageUrl {string} -- The URL of the image to display in the template.
            defaultAction {json} -- The default action executed when the template is tapped.
            buttons {list} -- An array of buttons to append to the template. A maximum of 3 buttons per element is supported.
        
        Returns:
            Json Object -- json object of element section
        """

        json_body = {"title": title, "image_url": imageUrl,
                     "subtitle": subTitle, "default_action": defaultAction,
                     "buttons": buttons}
        json_body = json.dumps(json_body)
        return json_body

    def createGenericTempleteJson(self, rec_ID, elementsList):
        """create the full generic template json
        
        Arguments:
            rec_ID {string} -- user id
            elementsList {list} -- An array of element objects that describe instances of the generic template to be sent.
                                   Specifying multiple elements will send a horizontally scrollable carousel of templates.
                                   A maximum of 10 elements is supported.
        
        Returns:
            Json Object -- json object of full generic template
        """

        self.type = "generic"
        json_body = {"recipient": {"id": rec_ID}, "message": {
            "attachment": {"type": "template", "payload":
                {"template_type": "generic",
                 "elements": elementsList}}}}
        json_body = json.dumps(json_body)
        return json_body

    def createListTempleteJson(self, rec_ID, elementsList,
                               topElementStyle="compact"):
        """create the full list template json
        
        Arguments:
            rec_ID {string} -- user id
            elementsList {list} -- An array of element objects that describe instances of the generic template to be sent.
                                   Specifying multiple elements will send a horizontally scrollable carousel of templates.
                                   A maximum of 10 elements is supported.
        
        Keyword Arguments:
            topElementStyle {string} -- Sets the format of the first list items. 
                                     Messenger web client currently only renders compact. (default: {"compact"})
        
        Returns:
            Json Object -- json object of full list template
        """

        self.type = "list"
        json_body = {"recipient": {"id": rec_ID}, "message": {"attachment": {"type": "template",
                                                                             "payload": {"template_type": "list",
                                                                                         "top_element_style": topElementStyle,
                                                                                         "elements": elementsList}}}}
        json_body = json.dumps(json_body)
        return json_body

    def createListTemplateWithButtonJson(self, rec_ID, elementsList,
                                         buttomButton, topElementStyle="compact"):
        """create the full list template json with buttom button
        
        Arguments:
            rec_ID {string} -- user id
            elementsList {list} -- An array of element objects that describe instances of the generic template to be sent.
                                   Specifying multiple elements will send a horizontally scrollable carousel of templates.
                                   A maximum of 10 elements is supported.
            buttomButton {list} -- Button to display on the list item. Maximum of 1 button is supported.
        
        Keyword Arguments:
            topElementStyle {str} -- Sets the format of the first list items. 
                                     Messenger web client currently only renders compact. (default: {"compact"})
        
        Returns:
            Json Object -- json object of full list template with buttom button
        """

        self.type = "list"
        json_body = {"recipient": {"id": rec_ID}, "message": {"attachment": {"type": "template",
                                                                             "payload": {"template_type": "list",
                                                                                         "top_element_style": topElementStyle,
                                                                                         "elements": elementsList,
                                                                                         "buttons": buttomButton}}}}
        json_body = json.dumps(json_body)
        return json_body

    def createButtonTemplateJson(self, rec_ID, text, buttonList):
        """create the full Button template json
        
        Arguments:
            rec_ID {string} -- user id
            text {string} -- UTF-8-encoded text of up to 640 characters. Text will appear above the buttons.
            buttonList {list} -- Set of 1-3 buttons that appear as call-to-actions.
        
        Returns:
            Json Object -- json object of full Button template
        """

        self.type = "button_temp"

        json_body = {"recipient": {"id": rec_ID}, "message": {"attachment": {"type": "template",
                                                                             "payload": {"template_type": "button",
                                                                                         "text": text,
                                                                                         "buttons": buttonList}}}}
        json_body = json.dumps(json_body)
        return json_body

    def createOpenGraphElementJson(self, elementUrl, button):
        """object that describes the open graph object to display.
        
        Arguments:
            elementUrl {string} -- String to display as the title of the list item.
                                   80 character limit. May be truncated if the title spans too many lines.
            button {list} -- An array of buttons to append to the template.
        
        Returns:
            Json Object -- json object of element section
        """

        json_body = {"url": elementUrl, "buttons": button}
        json_body = json.dumps(json_body)
        return json_body

    def createOpenGraphTemplateJson(self, rec_ID, elements):
        """create the full open graph template json
        
        Arguments:
            rec_ID {string} -- user id
            elements {list} -- Array of maximum 1 object that describes the open graph object to display.
        
        Returns:
             Json Object -- json object of open graph template
        """

        json_body = {"recipient": {"id": rec_ID}, "message": {
            "attachment": {"type": "template", "payload": {"template_type": "open_graph", "elements": elements}}}}
        json_body = json.dumps(json_body)
        return json_body

    def createMediaTemplateUrlJson(self, rec_ID, mediaType, Url, button):
        """create the full media template json
        
        Arguments:
            rec_ID {string} -- user id
            mediaType {string} -- The type of media being sent - image or video is supported.
            Url {string} -- The URL of the image
            button {list} -- An array of button objects to be appended to the template. A maximum of 1 button is supported.
        
        Returns:
            Json Object -- json object of media template
        """

        json_body = {"recipient": {"id": rec_ID}, "message": {"attachment": {"type": "template",
                                                                             "payload": {"template_type": "media",
                                                                                         "elements": [
                                                                                             {"media_type": mediaType,
                                                                                              "url": Url,
                                                                                              "buttons": button}]}}}}
        json_body = json.dumps(json_body)
        return json_body

    def createMediaTemplateIdJson(self, rec_ID, mediaType, attID):
        """create the full media template json by assest id
        
        Arguments:
            rec_ID {string} -- user id
            mediaType {string} -- The type of media being sent - image or video is supported.
            attID {string} -- The attachment ID of the image or video.
        
        Returns:
            Json Object -- json object of media template
        """

        json_body = {"recipient": {"id": rec_ID}, "message": {"attachment": {"type": "template",
                                                                             "payload": {"template_type": "media",
                                                                                         "elements": [
                                                                                             {"media_type": mediaType,
                                                                                              "attachment_id": attID}]}}}}
        json_body = json.dumps(json_body)
        return json_body



    def createReceiptTemplateSummaryJson(self, total_cost, subtotal="", shipping_cost="", total_tax=""):
        """The payment summary
        
        Arguments:
            total_cost {string} -- The total cost of the order, including sub-total, shipping, and tax.
        
        Keyword Arguments:
            subtotal {string} -- The sub-total of the order. (default: {""})
            shipping_cost {string} -- The shipping cost of the order. (default: {""})
            total_tax {string} -- The tax of the order. (default: {""})
        
        Returns:
            Json Object -- json object of Summary section
        """

        json_body = {"subtotal": subtotal, "shipping_cost": shipping_cost, "total_tax": total_tax,
                     "total_cost": total_cost}
        json_body = json.dumps(json_body)
        return json_body

    def createReceiptTemplateAdjustmentJson(self, name, amount):
        """An array of payment objects that describe payment adjustments, such as discounts.
        
        Arguments:
            name {string} -- Name of the adjustment.
            amount {string} -- The amount of the adjustment.
        
        Returns:
            Json Object -- json object of Adjustment section
        """

        json_body = {"name": name, "amount": amount}
        json_body = json.dumps(json_body)
        return json_body

    def createReceiptTemplateElementsJson(self, title, price, subtitle="", quantity="", currency="", image_url=""):
        """ Array of a maximum of 100 element objects that describe items in the order.
            Sort order of the elements is not guaranteed.
        
        Arguments:
            title {string} -- The name to display for the item.
            price {string} -- The price of the item. For free items, '0' is allowed.
        
        Keyword Arguments:
            subtitle {string} -- The subtitle for the item, usually a brief item description.
            quantity {string} -- The quantity of the item purchased.
            currency {string} -- The currency of the item price.
            image_url {string} -- The URL of an image to be displayed with the item.
        
        Returns:
            Json Object -- json object of element section
        """

        json_body = {"title": title, "subtitle": subtitle, "quantity": quantity, "price": price, "currency": currency,
                     "image_url": image_url}
        json_body = json.dumps(json_body)
        return json_body


    def createReceiptTemplateAddressJson(self, street_1, city, postal_code, state, country, street_2=""):
        """The shipping address of the order.
        
        Arguments:
            street_1 {string} -- The street address, line 1
            city {string} -- The city name of the address.
            postal_code {string} -- The postal code of the address.
            state {string} -- The state abbreviation for U.S. addresses, or the region/province for non-U.S. addresses.
            country {string} -- The two-letter country abbreviation of the address.
        
        Keyword Arguments:
            street_2 {string} -- [description] (default: {""})
        
        Returns:
            Json Object -- json object of address section
        """

        json_body = {"street_1": street_1, "street_2": street_2, "city": city, "postal_code": postal_code,
                     "state": state, "country": country}
        json_body = json.dumps(json_body)
        return json_body

    def createReceiptTemplateJson(self, rec_ID, recipient_name, order_number, currency, payment_method, order_url,
                                  summary, timestamp="",
                                  address="", adjustments="", elements=""):
        """create the full Receipt template json
        
        Arguments:
            rec_ID {string} -- rec_ID {string} -- user id
            recipient_name {string} -- The recipient's name.
            order_number {string} -- The order number. Must be unique.
            currency {string} -- The currency of the payment.
            payment_method {string} -- The payment method used. Providing enough information for 
                                       the customer to decipher which payment method and account they used is recommended.
                                       This can be a custom string, such as, "Visa 1234".
            order_url {string} -- The order number. Must be unique.
            summary {json} -- The payment summary
        
        Keyword Arguments:
            timestamp {string} -- Timestamp of the order in seconds. (default: {""})
            address {string} -- The shipping address of the order. (default: {""})
            adjustments {list} -- list of payment objects that describe payment adjustments, such as discounts. (default: {""})
            elements {list} -- Optional. Array of a maximum of 100 element objects that describe items in the order.
                              Sort order of the elements is not guaranteed. (default: {""})
        
        Returns:
            Json Object -- json object of Receipt template
        """

        json_body = {"recipient": {"id": rec_ID},
                     "message": {
                         "attachment": {
                             "type": "template",
                             "payload": {
                                 "template_type": "receipt",
                                 "recipient_name": recipient_name,
                                 "order_number": order_number,
                                 "currency": currency,
                                 "payment_method": payment_method,
                                 "order_url": order_url,
                                 "timestamp": timestamp,
                                 "address": address,
                                 "summary": summary,
                                 "adjustments": adjustments,
                                 "elements": elements}}}}
        json_body = json.dumps(json_body)
        return json_body
