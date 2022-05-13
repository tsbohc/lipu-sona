from gensim.test.utils import datapath
from gensim import utils
import gensim.models
from gensim.models import Word2Vec

model = gensim.models.Word2Vec.load('model_pu.wv')
wv = model.wv

def similarity(x, y):
    s = wv.similarity(x, y)
    print(x + '-' + y, str(round((s + 1)/2 * 100)) + '%', s)

similarity('pimeja', 'tenpo')
similarity('pimeja', 'kule')

similarity('walo', 'tenpo')
similarity('walo', 'kule')


similarity('kasi', 'kule')
similarity('kasi', 'tenpo')

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
