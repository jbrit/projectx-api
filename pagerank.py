from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from word_process import process_sentence


def get_document_scores(search, projects):
    search = process_sentence(search)
    topics = list(map(lambda p: process_sentence(p["topic"]), projects))
    doc_vectors = TfidfVectorizer().fit_transform([search] + topics)
    cosine_similarities = linear_kernel(doc_vectors[0:1], doc_vectors).flatten()
    document_scores = [item.item() for item in cosine_similarities[1:]]

    with_search = [ None for _ in projects ]

    for i in range(len(with_search)):
        with_search[i] = dict(projects[i])
        with_search[i]["score"] = document_scores[i]

    return document_scores, with_search
