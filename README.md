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

##Transcrips
Test case 1 : per se
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Iteration 1
Query     = per se
Precision = 0 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

=================================================================================
Result 1
URL: https://www.thomaskeller.com/perseny
Title: Per Se | Thomas Keller Restaurant Group
Summary: Per Se. Per Se Front Door. center. About. About; Restaurant · Team · Info & Directions · Gift Experiences · Reservations; Menus & Stories. Menus & Stories
Relevant (Y/N)y
=================================================================================
Result 2
URL: https://en.wiktionary.org/wiki/per_se
Title: per se - Wiktionary
Summary: In and of itself; by itself; without determination by or involvement of extraneous factors; as such quotations ▽synonym △ · (philosophy) Being a thing that ...
Relevant (Y/N)n
=================================================================================
Result 3
URL: https://www.exploretock.com/perse
Title: Per Se - New York, NY | Tock
Summary: Opened in 2004, Per Se is Thomas Keller's acclaimed interpretation of The French Laundry in the Deutsche Bank Center at Columbus Circle.
Relevant (Y/N)y
=================================================================================
Result 4
URL: https://www.instagram.com/perseny/?hl=en
Title: Per Se (@perseny) • Instagram photos and videos
Summary: Chef Thomas Keller's 3-Star Michelin restaurant overlooking Columbus Circle & Central Park located in New York City. exploretock.com/perse. 882 posts.
Relevant (Y/N)y
=================================================================================
Result 5
URL: https://www.yelp.com/biz/per-se-new-york
Title: PER SE - 7270 Photos & 1824 Reviews - Food near New York, NY ...
Summary: 1824 reviews of Per Se "This is Thomas Keller's new resturant in New York. A must if you can get a reservation."
Relevant (Y/N)y
=================================================================================
Result 6
URL: https://www.merriam-webster.com/dictionary/perse
Title: Perse Definition & Meaning - Merriam-Webster
Summary: adjective (1) · ˈpərs · of a dark grayish blue resembling indigo ; adverb. (ˌ)pər-ˈsā,. also per-ˈsā,. or. (ˌ)pər-ˈsē · by, of, or in itself or oneself or ...
Relevant (Y/N)n
=================================================================================
Result 7
URL: https://guide.michelin.com/us/en/new-york-state/new-york/.../per-se
Title: Per Se – New York - a MICHELIN Guide Restaurant
Summary: Per Se – a Three MICHELIN Stars: Exceptional cuisine, worth a special journey! restaurant in the 2022 MICHELIN Guide USA. The MICHELIN inspectors' point of ...
Relevant (Y/N)y
=================================================================================
Result 8
URL: https://dictionary.cambridge.org/dictionary/english/per-se
Title: PER SE | English meaning - Cambridge Dictionary
Summary: 7 days ago ... per se definition: 1. by or of itself: 2. by or of itself: 3. by or of itself: . Learn more.
Relevant (Y/N)n
=================================================================================
Result 9
URL: https://www.persegroup.com/
Title: Per Se Group
Summary: Per Sé is a leading workforce solution to the Energy and Industrial markets. Our technology, and recruitment expertise, seamlessly match talented people in ...
Relevant (Y/N)n
=================================================================================
Result 10
URL: https://www.vocabulary.com/dictionary/per%20se
Title: Per se - Definition, Meaning & Synonyms | Vocabulary.com
Summary: Per se is the phrase to use when you want to refer to a particular thing on its own. It is not this Latin phrase, per se, that is important, but rather the ...
Relevant (Y/N)n

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Iteration 2
Query     = restaurant michelin per se
Precision = 0.5 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

=================================================================================
Result 1
URL: https://guide.michelin.com/us/en/new-york-state/new.../restaurant/per-se
Title: Per Se – New York - a MICHELIN Guide Restaurant
Summary: Three MICHELIN Stars: Exceptional cuisine, worth a special journey! An experience at Thomas Keller's Per Se is one to be savored, recounted and remembered.
Relevant (Y/N)y
=================================================================================
Result 2
URL: https://www.thomaskeller.com/perseny
Title: Per Se | Thomas Keller Restaurant Group
Summary: Per Se. Per Se Front Door. center. About. About; Restaurant · Team · Info & Directions · Gift Experiences · Reservations; Menus & Stories. Menus & Stories
Relevant (Y/N)y
=================================================================================
Result 3
URL: https://en.wikipedia.org/wiki/Per_Se_(restaurant)
Title: Per Se (restaurant) - Wikipedia
Summary: Per Se (restaurant) · Michelin Guide: 3 Michelin stars · The New York Times: 2 out of 4 stars · The World's 50 Best Restaurants: 81st.
Relevant (Y/N)y
=================================================================================
Result 4
URL: https://andershusa.com/per-se-new-york-thomas-keller-most-expensive-meal- ever/
Title: Video: Per Se - Our Most Expensive Meal Ever
Summary: Mar 15, 2022 ... Chef Thomas Keller's flagship NYC restaurant, Per Se, is his tribute to French Laundry on the east coast. It has held three Michelin stars ...
Relevant (Y/N)y
=================================================================================
Result 5
URL: https://www.businessinsider.com/nyc-best-michelin-restaurants-le-bernardin- per-se-2018-11
Title: Le Bernardin and Per Se Have Had 3 Michelin Stars for 14 Years ...
Summary: Dec 6, 2018 ... Two of the restaurants, Le Bernardin and Per Se, have won the highest Michelin rating 14 times, every year since the restaurant guide was ...
Relevant (Y/N)y
=================================================================================
Result 6
URL: https://www.instagram.com/perseny/?hl=en
Title: Per Se (@perseny) • Instagram photos and videos
Summary: Chef Thomas Keller's 3-Star Michelin restaurant overlooking Columbus Circle & Central Park located in New York City. exploretock.com/perse. 882 posts.
Relevant (Y/N)y
=================================================================================
Result 7
URL: https://www.cbsnews.com/.../michelin-starred-restaurant-per-se-racks-up-c- rating-from-health-department/
Title: Michelin-Starred Restaurant Per Se Racks Up C Rating From Health ...
Summary: Mar 4, 2014 ... Per Se is one of only seven New York City restaurants to earn three Michelin stars, and The New York Times called it the city's best restaurant ...
Relevant (Y/N)y
=================================================================================
Result 8
URL: https://ny.eater.com/2022/10/6/.../michelin-restaurants-nyc-stars-2022
Title: NYC Michelin Stars 2022: The Full List - Eater NY
Summary: Oct 6, 2022 ... Three-stars restaurants. Chef's Table at Brooklyn Fare. Eleven Madison Park. Le Bernardin. Masa. Per Se · Two-star restaurants. Al Coro (new).
Relevant (Y/N)y
=================================================================================
Result 9
URL: https://www.nytimes.com/2016/01/13/dining/pete-wells-per-se-review.html
Title: At Thomas Keller's Per Se, Slips and Stumbles - The New York Times
Summary: Jan 12, 2016 ... Dinner or lunch at this grand, hermetic, self-regarding, ungenerous restaurant brings a protracted march of many dishes. In 2004, the year Per ...
Relevant (Y/N)y
=================================================================================
Result 10
URL: https://www.exploretock.com/perse
Title: Per Se - New York, NY | Tock
Summary: The restaurant is Chef Keller's second three-Michelin-starred property featuring Chef's tasting menu and a vegetable tasting menu using classic French ...
Relevant (Y/N)y
Precesion got! Your final query is restaurant michelin per se
