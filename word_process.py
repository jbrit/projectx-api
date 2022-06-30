import nltk
import ssl

# RUN on First Try
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download("stopwords")
nltk.download("punkt")

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

ps = PorterStemmer()

stop_words = set(stopwords.words('english'))

stem_tokens = lambda tokens: list(map(ps.stem,tokens))

def tokenize(sentence):
    return word_tokenize(sentence)

def filter_stop_words(tokens):
    return [w for w in tokens if not w.lower() in stop_words]

def filter_small_words(tokens):
    return [w for w in tokens if len(w) > 3]
    

def process_sentence(sentence):
    word_tokens = tokenize(sentence)
    without_stop = filter_stop_words(word_tokens)
    without_small = filter_small_words(without_stop)
    stemmed = stem_tokens(without_small)
    return " ".join(stemmed)
    