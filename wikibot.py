import wikipedia

def scrape(name='Mumbai',length=2):
    result = wikipedia.summary(name, sentences=length)
    return result

print(scrape())



