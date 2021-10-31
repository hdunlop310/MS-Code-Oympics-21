import requests
from bs4 import BeautifulSoup
from monkeylearn import MonkeyLearn
import nltk
from nltk.corpus import wordnet
import ssl


# try:
#    _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#    pass
# else:
#    ssl._create_default_https_context = _create_unverified_https_context

# nltk.download()

def headline_scraper():
    URL = "https://www.theguardian.com/uk"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="headlines")
    job_elements = results.find_all("a", class_="u-faux-block-link__overlay js-headline-text")

    headlines = []

    for element in job_elements:
        element = str(element)
        end_opening_tag_index = list(element).index(">")
        begin_closing_tag_index = list(element)[end_opening_tag_index + 1:].index("<")
        title_with_closing_tag = list(element)[end_opening_tag_index + 1:]
        title = "".join(list(title_with_closing_tag)[:begin_closing_tag_index])
        headlines.append(title)

    return headlines


def sentiment_classifier(word):
    ml = MonkeyLearn('')  # Monkey Learn API Key Here
    model_id = 'cl_pi3C7JiL'
    result = ml.classifiers.classify(model_id, word)
    result = result.body[0]["classifications"][0]["tag_name"]
    return result


def headline_changer(headline):
    negative_word_found = False
    for word in headline.split():
        if not word.istitle():
            if sentiment_classifier([word]) == "Negative" or sentiment_classifier([word]) == "Neutral":
                negative_word_found = True
                if negative_to_positive(word) is False:
                    continue
                else:
                    new_word = negative_to_positive(word)
                    headline.replace(word, new_word)
        else:
            continue

    if not negative_word_found:
        print("No negative words found.")
        return headline
    return headline


def negative_to_positive(word):
    for syn in wordnet.synsets(word):
        for lm in syn.lemmas():
            if lm.antonyms():
                return lm.antonyms()[0].name()
            else:
                return False


if __name__ == "__main__":
    headlines = headline_scraper()
    headline = headline_changer(headlines[0])
    print(headline)
