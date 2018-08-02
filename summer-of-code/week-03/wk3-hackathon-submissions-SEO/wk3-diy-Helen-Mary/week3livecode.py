import pandas as pd
import nltk as nl

# Load seed keywords on a dataframe or list input file: seedlist.txt
seed  = open('seedlist.txt', 'r') 

#Initialize 
GoogleQueries=[]

for line in seed:
    print(line)
    GoogleQueries.append('http://www.google.com/search?start=0&num=10&q='+line)

# Create Google Search URLs for each seed keyword on the list and list as another dataframe
#https://developers.google.com/custom-search/docs/xml_results
# Sample Query URL for Google: http://www.google.com/search?start=0&num=10&q=red+sox&output=xml

print(GoogleQueries)

# Scrape the links from each Google URL (for this use case just first page of results muna)

# Access the scraped links and store each page via Puppeteer API? 

# List all the <h> and <p> tagged text and use NLTK to write a concordance of words for each link 

# Aggregate all outputs in one csv file 
