import pandas as pd

'''print(pd.__version__)
simpsons = pd.read_html("https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes")
print(simpsons[1])'''



url = "https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes"

# Pass a browser User-Agent header so Wikipedia doesn't block the request
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

simpsons = pd.read_html(url, storage_options=headers)

# Verify it works by printing the first table found
print(simpsons[0].head())
