import numpy
import gensim
import nltk
import warnings
from nltk.tokenize import sent_tokenize, word_tokenize
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity

#nltk.download('punkt')
warnings.filterwarnings(action='ignore')
file_names = ["../../sample-data/Albert Einstein___Sidelights on Relativity.txt",
              "../../sample-data/James Fenimore Cooper___The Chainbearer.txt"]


def extract_sentence_tokens_from_file(file_names):
    data = []
    for file_name in file_names:
        sample = open(file_name)
        s = sample.read()
        # Replaces escape character with space
        f = s.replace("\n", " ")
        # iterate through each sentence in the file
        for i in sent_tokenize(f):
            temp = []

            # tokenize the sentence into words
            for j in word_tokenize(i):
                temp.append(j.lower())

            data.append(temp)
    return data


data = extract_sentence_tokens_from_file(file_names)

#print(data[:3])

# Create CBOW model
model1 = gensim.models.Word2Vec(data, min_count = 1, vector_size=100, window = 5)
model1.save("../../../word2vec1.model")

# Create Skip Gram model
model2 = gensim.models.Word2Vec(data, min_count=1, vector_size=100, window=5, sg=1)
model1.save("../../../word2vec2.model")

word1 = 'light'
word2 = 'relativity'

def wv_word_sim(word1, word2, model):
    vector1 = model.wv[word1]  # get numpy vector of a word
    vector2 = model.wv[word2]  # get numpy vector of a word
    sim = cosine_similarity([vector1], [vector2])
    return sim

csim = wv_word_sim(word1, word2, model1)
print(csim)

csim = wv_word_sim(word1, word2, model2)
print(csim)




