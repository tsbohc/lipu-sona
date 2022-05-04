from gensim.test.utils import datapath
from gensim import utils
import gensim.models
from gensim.models import Word2Vec

# class corpus_iterator:
#     def __iter__(self):
#         corpus_path = 'corpus'
#         for line in open(corpus_path):
#             yield utils.simple_preprocess(line)
#
# corpus = corpus_iterator()
# model = Word2Vec(sentences=corpus, vector_size=190)
#
# model.save('model.wv')

model = gensim.models.Word2Vec.load('model.wv')
wv = model.wv

print(wv.most_similar('palisa'))
# print('---')
# print(wv.most_similar(positive=['suno', 'lete'], negative=['seli']))





# ---

# import pandas as pd
#
# def tsne_export(model):
#     labels = []
#     tokens = []
#
#     for word in model.wv.key_to_index:
#         tokens.append(model.wv[word])
#         labels.append(word)
#
#     tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500, random_state=23)
#     tsne_result = tsne_model.fit_transform(tokens)
#
#     x = []
#     y = []
#     for value in tsne_result:
#         x.append(value[0])
#         y.append(value[1])
#
#     # tsne_result_data = pd.DataFrame({'tsne_1': x, 'tsne_2': y, 'label': labels})
#
#     print("{")
#     for i in range(len(x)):
#         print("'" + labels[i] + "': [" + str(x[i]) + ", " + str(y[i]) + "]")
#     print("}")
#
# tsne_export(model)
