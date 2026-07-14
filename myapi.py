import nlpcloud
class API:
    def __init__(self):
        self.client = nlpcloud.Client("gpt-oss-120b", "YOUR_API_KEY", gpu=True)

    
    def sentiment_analysis(self,text):
       
        response=self.client.sentiment(text,target="NLP Cloud")
        return response
        # L = []
        # for i in response['scored_labels']:
        #     L.append(i['score'])

        # index = sorted(list(enumerate(L)),key=lambda x:x[1],reverse=True)[0][0]

        # print(response['scored_labels'][index]['label'])

    def NER(self,text,entity):

        response=self.client.entities(text,searched_entity=entity)
        return response

