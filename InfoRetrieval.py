import sys
from googleapiclient.discovery import build
class InfoRetrieval:
    def main():
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
        print(res["items"][0].keys())
    if __name__ == '__main__':
        main()
