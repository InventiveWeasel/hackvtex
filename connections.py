import requests

class ConnectionManager:
    def __init__(self, url):
        self.serverURL = url
    
    def getDescription(self,descID):
        PARAMS = {'codigo':descID}
        r = requests.get(url=self.serverURL, params=PARAMS)
        print(r.content)
        desc = r.content.decode("utf-8")
        #remove breakline
        auxBR = desc.find("<")

        return desc[:auxBR]
