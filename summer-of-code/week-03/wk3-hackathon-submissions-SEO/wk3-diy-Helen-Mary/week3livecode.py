import pandas as pd
import nltk as nl

# Load seed keywords on a dataframe or list input file: seedlist_clean.csv
seedlist = pd.read_csv('seedlist_clean.csv')
print seedlist


# Create Google Search URLs for each seed keyword on the list and list as another dataframe

# Scrape the links from each Google URL (for this use case just first page of results muna)

# Access the scraped links and store each page via Puppeteer API? 

# List all the <h> and <p> tagged text and use NLTK to write a concordance of words for each link 

# Aggregate all outputs in one csv file 
