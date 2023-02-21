# InfoRetrieval


## Authors

Ziyu Liu, zl3220\
Zelin Wang, zw2852


## Project files

- InfoRetrieval.py

## How to run
1. Clone the repository:
```bash
git clone https://github.com/samuelliuliuliu666/cs6111-project1
```

2. Install dependencies:
```bash
pip install google-api-python-client
pip install nltk
```

3. Download nltk stopwords and punkt:
```bash
python -m nltk.downloader stopwords punkt
```

4. Add your Google Custom Search Engine JSON API Key and Engine ID to InfoRetrieval.py:
```python
api_key = "AIzaSyBe5rpBXOaw4IW8piccWUA0VZ9gNhUMWgY"
eng_id = "497c7780958f3ec5b"
```

5. Run the program:
```bash
python InfoRetrieval.py AIzaSyBe5rpBXOaw4IW8piccWUA0VZ9gNhUMWgY 497c7780958f3ec5b [PRECISION] [QUERY]
```

## Internal design
The `InfoRetrieval` class contains several methods to perform the search and query modification. `tokenize` method is used to tokenize the search query and `removeNonLetter` method is used to remove non-letter characters. `removeStopWords` method is used to remove stop words. `clean` method returns a list of clean words from the documents. `cal_tf` method computes the term frequency of every word in a document, and `cal_idf` method computes the IDF of all the words in one document. `cal_tfIdf` method calculates the tfIDF of all words in relevant documents, and `get_top2` method returns the 2 words with the highest tfIdf. `reordering` method reorders the query based on the average positions of the words in the documents. `feedback` method records user's feedback on whether a document is relevant or not.

The `main` method performs the search and query modification. The desired precision is set by the `threshold` parameter. If precision is not achieved, the program keeps running until the desired precision is met or no relevant results are returned. In each iteration, `feedback` method is called to get the relevant documents, and `cal_tfIdf`, `get_top2`, and `reordering` methods are used to modify the search query. Finally, when the desired precision is achieved, the program outputs the final query.

## Query-modification method
The query-modification method works as follows:

1. Get feedback from the user on the first set of results.
2. Calculate the tfIdf of all words in the relevant documents.
3. Get the two words with the highest tfIdf.
4. Add the two words to the query.
5. Reorder the query based on the average positions of the words in the relevant documents.
6. Repeat from step 1 until the desired precision is achieved or no relevant results are returned.

## Google Custom Search Engine JSON API Key and Engine ID
API Key: "AIzaSyBe5rpBXOaw4IW8piccWUA0VZ9gNhUMWgY"

Engine ID: "497c7780958f3ec5b"

## License

[MIT](https://choosealicense.com/licenses/mit/)


