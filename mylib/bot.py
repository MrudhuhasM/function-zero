import wikipedia

def scrape(name='Vizag',length=2):
    result = wikipedia.summary(name, sentences=length)
    return result
