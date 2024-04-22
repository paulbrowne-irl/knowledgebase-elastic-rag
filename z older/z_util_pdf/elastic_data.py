import json
from langchain.text_splitter import CharacterTextSplitter

class ElasticData:

    name = ""
    text = ""

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    
    def toDocument(self):
        doc_creator = CharacterTextSplitter()

        newDoc =doc_creator.toDocument(self.text)
        newDoc
        
        return newDoc 