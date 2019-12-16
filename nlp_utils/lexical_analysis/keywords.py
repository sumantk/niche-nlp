# https://github.com/boudinfl/pke
# https://pdfs.semanticscholar.org/cbcd/6ce6b44f729acaf7b0e345c77901177c8ac7.pdf


import pke

def extract_pke_keywords():
    # initialize keyphrase extraction model, here TopicRank
    extractor = pke.unsupervised.TopicRank()
    # load the content of the document, here document is expected to be in raw
    # format (i.e. a simple text file) and preprocessing is carried out using spacy
    extractor.load_document(input='/path/to/input.txt', language='en')
    # keyphrase candidate selection, in the case of TopicRank: sequences of nouns
    # and adjectives (i.e. `(Noun|Adj)*`)
    extractor.candidate_selection()
    # candidate weighting, in the case of TopicRank: using a random walk algorithm
    extractor.candidate_weighting()
    # N-best selection, keyphrases contains the 10 highest scored candidates as
    # (keyphrase, score) tuples
    keyphrases = extractor.get_n_best(n=10)


extract_pke_keywords()