from wikibot import scrape

def test_scrape():
    assert "Mumbai" in scrape("Mumbai")

    