import requests
import json
import os 
from moviepy.editor import AudioFileClip
import speech_recognition as sr
from .handlers.jsonHandler   import jsonHandler
from .structure.simpleMsg    import simpleMsg
from .structure.quickReplies import quickReplies
from .structure.templates    import templates
from .structure.buttons      import buttons

class messenger(jsonHandler, simpleMsg, quickReplies, templates, buttons):
    """[summary]
    
    Arguments:
        jsonHandler {class} -- operate on received json
        simpleMsg {class} -- responsible for simple messages
        quickReplies {class} -- responsible for quick Replies
        templates {class} -- responsible for templates
        buttons {class} -- responsible for buttons

    """

    def __init__(self):

        self.ACCESS_TOKEN = ""
        self.VERIFY_TOKEN = ""
        self.URL_BASE = "https://graph.facebook.com/v2.6/me/"
        self.URL_BASE_TEMPS = "https://graph.facebook.com/me/"
        self.post_url = "messages?access_token="
        self.assest_url = "message_attachments?access_token="

    def URL_TO_POST(self, url):
        """return the required url to the api
        
        Arguments:
            url {string} -- url to api
                    
        Returns:
            string -- url to api
        """
        return self.URL_BASE + url + self.ACCESS_TOKEN

    def Verify_Token(self, token):
        """verfiy toke in when setup webhooks
        
        Arguments:
            token {string} -- token to be verfied
        
        Returns:
            bool -- if the toke is coorect or not
        """
        if (token == self.VERIFY_TOKEN):
            return True
        else:
            return False

    def sender(self, jsonToSend, assest=False):
        """send json to facebook api
        
        Arguments:
            jsonToSend {json} -- json of any kind to send
        
        Keyword Arguments:
            assest {bool} -- if you want to send assests set it to true (default: {False})
        
        Returns:
            requst object -- return the reponse of the sending
        """

        post_message_url = ""

        if assest:
            post_message_url = self.URL_TO_POST(self.assest_url)
        else :
            post_message_url = self.URL_TO_POST(self.post_url)

        headers = {"Content-Type": "application/json"}
        req = requests.post(post_message_url, headers=headers, data=jsonToSend, timeout=20)

        return req 

    def savingAssests(self, type_of_content, url):
        """save assests to facebook server
        
        Arguments:
            type_of_content {string} -- tyoe if content image, video, audio, file
            url {string} -- url of the media
        
        Returns:
            string -- id of assest to use it in buttons,temps,...etc
        """

        json_body = { "message": {"attachment": {"type": type_of_content, "payload": {"is_reusable": "true", "url": url}}}}
        json_body = json.dumps(json_body)
        req = self.sender(json_body, assest=True)
        return req.json()["attachment_id"]

    def addObject(self, obje, arrayOfObjects=[]):
        """add object to array
        
        Arguments:
            obje {object} -- any object to be added
        
        Keyword Arguments:
            arrayOfObjects {list} -- list of objects  (default: {[]})
        
        Returns:
            list -- return list after being added to list
        """

        arrayOfObjects = arrayOfObjects + [obje]
        return arrayOfObjects

    def downloadFile(self, id, url):
        """rebonsible for downloading 
        
        Arguments:
            id {string} -- id of user
            url {string} -- url of file
        
        Returns:
            string -- file's name
        """

        local_filename = str(id)+".mp4"
        r = requests.get(url, stream=True)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        return local_filename

    def covertMp4Towav(self, inputName, outputName):
        """convert mp4 file to wave
        
        Arguments:
            inputName {string} -- file name
            outputName {string} -- file name after converting
        """

        audioclip = AudioFileClip(inputName)
        audioclip.write_audiofile(outputName)

    def voiceNoteToText(self, id, url, lan="en-US"):
        """extract text from voice note
        
        Arguments:
            id {string} -- user id
            url {string} -- url of the voice note
        
        Keyword Arguments:
            lan {string} -- language of the voice note (default: {"en-US"})
        
        Returns:
            string -- text ininside voice note
        """

        nameIn  = str(id)+".mp4"
        nameOut = str(id)+".wav"

        self.downloadFile(id, url)
        self.covertMp4Towav(nameIn, nameOut)

        r = sr.Recognizer()
        with sr.AudioFile(nameOut) as source:
            audio = r.record(source)

        command = r.recognize_google(audio, language=lan)

        return command
