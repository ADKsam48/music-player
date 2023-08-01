import pyshorteners
link = input("paste your link in here \n")
shortner = pyshorteners.Shortener()
short_link = shortner.tinyurl.short(link)
print("Here is a url shortener for the given url mentioned \n", short_link)