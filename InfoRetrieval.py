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
    
    def reordering(self,query,relevant_docs):    
        # Extract word positions
        word_positions = {}
        for word in query:
            positions = []
            for doc in relevant_docs:
                for i, token in enumerate(doc):
                    if token == word:
                        positions.append(i)
            word_positions[word] = positions    
        # Calculate average positions
        avg_positions = {}
        for word in word_positions:
            positions = word_positions[word]
            avg_positions[word] = sum(positions) / len(positions) if positions else float('inf')
        
        # Reorder the query
        sorted_words = sorted(query, key=lambda w: avg_positions[w])
        reordered_query = ' '.join(sorted_words)
        return reordered_query
    

    def feedback(self,res):
        '''
        Records user's feedback on wheter a document is relevant or not 
            Parameter: res - a dic returned by Google Search API
            Returns: all relevant documents
        '''
        all_results = res['items']
        relevant_docs = []
        all_docs = []
        for i in range (len(all_results)):
            print(
            "=================================================================================")
            print("Result " + str(i+1))
            print("URL: " + all_results[i]['formattedUrl'])
            print("Title: " + all_results[i]["title"])
            print("Summary: " + all_results[i]['snippet'])
            
            feedback = input('Relevant (Y/N)')
            while feedback.lower() != 'y' and feedback.lower() != 'n':
                print("Please enter a valid input! (Y/N)")
                feedback = input('Relevant (Y/N)')
            title = self.clean(all_results[i]['title'])
            snip = self.clean(all_results[i]['snippet'])
            words = title + snip
            if feedback.lower() == 'y':
                relevant_docs.append(words)
            all_docs.append(words)
        return relevant_docs,all_docs
        

    def main(self):
        # api_key = sys.argv[1]
        # eng_id = sys.argv[2]
        # threshold = float(sys.argv[3])
        # query = sys.argv[4]
#         service = build("customsearch", "v1",
#                 developerKey=api_key)
# #dict_keys(['kind', 'title', 'htmlTitle', 'link', 'displayLink', 
# #'snippet', 'htmlSnippet', 'formattedUrl', 'htmlFormattedUrl', 'pagemap'])
#         res = service.cse().list(
#             q=query,
#             cx=eng_id,
#         ).execute()
        # print(res["items"][0]['title'])
        # snip = res["items"][0]['snippet']
        # print(snip)
        # cleaned = self.clean(snip)
        # print(cleaned)
        # dic = self.cal_tf(cleaned)
        # print(dic)
        # print(res["items"][0]['htmlSnippet'])
        # all_docs = []
        # for doc in res["items"]:
        #     title = self.clean(doc['title'])
        #     snip = self.clean(doc['snippet'])
        #     words = title + snip
        #     all_docs.append(words)
        # relevant_docs = [all_docs[1],all_docs[3],all_docs[4]]
        # tf_idf = self.cal_tfIdf(relevant_docs,all_docs)
        # print(tf_idf)
        # two_words = self.get_top2(tf_idf,["lebron"])
        # print(two_words)
        # new_query = [query]+two_words
        # print(new_query)
        # sorted_query = self.reordering(new_query,relevant_docs)
        # print(sorted_query)

        # relevant_docs = self.feedback(res)
        # print(relevant_docs)
        precision = 0
        iteration = 1
        success = True
        api_key = sys.argv[1]
        eng_id = sys.argv[2]
        threshold = float(sys.argv[3])
        query = sys.argv[4]
        # Loop when desired precision has not been reached and Google API returns some results 
        while(precision < threshold):
            service = build("customsearch", "v1", developerKey=api_key)
            res = service.cse().list(q=query,cx=eng_id).execute()
            # Output iteration number and search query
            print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            print("Iteration {}\nQuery     = {}\nPrecision = {} ".format(iteration,query,precision))
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
            relevant_docs,all_docs = self.feedback(res) 
            # Check if query was successful
            if len(relevant_docs) == 0:
                print("\nOops! Even google has no idea about what you're looking for")
                print("Please enter another query so that google can return at least one relevant result for you!")
                success = False
                break
            #check if precision has achieved 
            precision = len(relevant_docs)/len(all_docs)
            if precision >= threshold:
                break

            tfIdf = self.cal_tfIdf(relevant_docs,all_docs)
            two_words = self.get_top2(tfIdf,query.split())
            new_query = query.split() + two_words
            reordered_query = self.reordering(new_query,relevant_docs)
            query = reordered_query
            iteration += 1

        if success:
            print("Precesion got! Your final query is " + query)

if __name__ == '__main__':
    ir = InfoRetrieval()
    ir.main()
