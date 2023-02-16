import sys
from googleapiclient.discovery import build
import string 
import nltk
nltk.download('stopwords')
nltk.download('punkt')
class InfoRetrieval:

    def tokenize(self,raw_str):
        tokens = nltk.tokenize.word_tokenize(raw_str)
        lower_tokens = [x.lower() for x in tokens]
        return lower_tokens

    def removeNonLetter(self,tokens):
        #removes punctuations from an input string 
        new_list = []
        for token in tokens:
            append = True
            for c in token:
                if not(c.isalpha()):
                    append = False
            if append:
                new_list.append(token)     
        return new_list
    
    def removeStopWords(self,tokens):
        #removes all stopwords from tokens. 
        cleaned_token = [x for x in tokens if not x in nltk.corpus.stopwords.words()]
        return cleaned_token

    def clean(self,raw_str):
        lower_tokens = self.tokenize(raw_str)
        new_list = self.removeNonLetter(lower_tokens)
        cleaned_tokens = self.removeStopWords(new_list)
        return cleaned_tokens

    
    def cal_tf(self):
        pass

    def main(self):
        api_key = sys.argv[1]
        eng_id = sys.argv[2]
        threshold = float(sys.argv[3])
        query = sys.argv[4]
        service = build("customsearch", "v1",
                developerKey=api_key)
#dict_keys(['kind', 'title', 'htmlTitle', 'link', 'displayLink', 
#'snippet', 'htmlSnippet', 'formattedUrl', 'htmlFormattedUrl', 'pagemap'])
        res = service.cse().list(
            q=query,
            cx=eng_id,
        ).execute()
        print(res["items"][0]['title'])
        snip = res["items"][0]['snippet']
        print(snip)
        print(self.clean(snip))
        print(res["items"][0]['htmlSnippet'])

if __name__ == '__main__':
    ir = InfoRetrieval()
    ir.main()
