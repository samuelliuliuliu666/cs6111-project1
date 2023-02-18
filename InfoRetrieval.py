import sys
from googleapiclient.discovery import build
import string 
import nltk
import math
from collections import Counter
nltk.download('stopwords')
nltk.download('punkt')
class InfoRetrieval:

    def tokenize(self,raw_str):
        tokens = nltk.tokenize.word_tokenize(raw_str)
        lower_tokens = [x.lower() for x in tokens]
        return lower_tokens
    
    #removes punctuations from an input string
    def removeNonLetter(self,tokens):
        new_list = []
        for token in tokens:
            append = True
            for c in token:
                if not(c.isalpha()):
                    append = False
            if append:
                new_list.append(token)     
        return new_list
    
    #removes all stopwords from tokens.
    def removeStopWords(self,tokens):
        cleaned_token = [x for x in tokens if not x in nltk.corpus.stopwords.words()]
        return cleaned_token
    #returns a list containg all clean words from a doc
    def clean(self,raw_str):
        lower_tokens = self.tokenize(raw_str)
        new_list = self.removeNonLetter(lower_tokens)
        cleaned_tokens = self.removeStopWords(new_list)
        return cleaned_tokens

    #computes the term frequency of every word in a document
    #returns a dictionary which contains counts of each word
    def cal_tf(self,doc):
        tf = Counter(doc)
        return tf
    
    #computes the idf of all the words in one document 
    #returns a dictionary which contains idf if each word in a document 
    #doc : []   all_docs: [[doc1],doc[2],doc[3]...]
    def cal_idf(self,doc,all_docs):
        idf_dic = {} 
        for item in doc:
            count = 0
            for dc in all_docs:
                if item in dc:
                    count += 1
            idf = math.log10(len(all_docs)/count)    
            if item not in idf_dic.keys():
                idf_dic[item] =  idf
        return idf_dic
    
    #calculates the tfIdf of all words in relevant documents
    def cal_tfIdf(self,relevant_docs,all_docs):
        tfIdf = {}
        for doc in relevant_docs:
            tf = self.cal_tf(doc)
            idf_dic = self.cal_idf(doc,all_docs)
            for key in tf.keys():
                tf_idf = math.log10(1+tf[key])*idf_dic[key]
                if key not in tfIdf.keys():
                    tfIdf[key] = tf_idf
                else:
                    tfIdf[key] += tf_idf
        return tfIdf
    
    #get the 2 words with highest tfIdf 
    #query : list of words ; 
    def get_top2(self,tfIdf,query):
        sorted_words = sorted(tfIdf.items(), key=lambda x: x[1], reverse=True)
        print(sorted_words)
        two_words = []
        for item in sorted_words:
            if item not in query and len(two_words) < 2:
                two_words.append(item[0])
        return two_words
    
    def reordering(self,query,):
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
        cleaned = self.clean(snip)
        print(cleaned)
        dic = self.cal_tf(cleaned)
        print(dic)
        print(res["items"][0]['htmlSnippet'])
        all_docs = []
        for doc in res["items"]:
            title = self.clean(doc['title'])
            snip = self.clean(doc['snippet'])
            words = title + snip
            all_docs.append(words)
        relevant_docs = [all_docs[1],all_docs[3],all_docs[4]]
        tf_idf = self.cal_tfIdf(relevant_docs,all_docs)
        print(tf_idf)
        two_words = self.get_top2(tf_idf,["lebron"])
        print(two_words)

if __name__ == '__main__':
    ir = InfoRetrieval()
    ir.main()
