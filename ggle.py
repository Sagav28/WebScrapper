from googlesearch.googlesearch import GoogleSearch
a=raw_input("Enter the term to Search")
response = GoogleSearch().search(a)
for result in response.results:
    print result.url