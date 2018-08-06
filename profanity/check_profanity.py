import urllib

def read_text():
    quotes = open("C:\Users\Konstantinos\Desktop\movie_quotes.txt")
    read_quotes = quotes.read()
    print(read_quotes)
    quotes.close()
    check_text_profanity(read_quotes)

def check_text_profanity(text):
    connectionToWebSite = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    profanity_result = connectionToWebSite.read()
    connectionToWebSite.close()
    if "true" in profanity_result:
        print("Profanity Alert!!")
    elif "false" in profanity_result:
        print("Thid document has no curse words")
    else:
        print("Could not scan the document properly")
    
read_text()
