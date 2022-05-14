from gensim.test.utils import datapath
from gensim import utils
import gensim.models
from gensim.models import Word2Vec

model = gensim.models.Word2Vec.load('model_pu.wv')
wv = model.wv

def sc(x, y):
    s = wv.similarity(x, y)
    print(x + '-' + y, str(round((s + 1)/2 * 100)) + '%', round(s, 2))

def most_similar(x):
    s = wv.most_similar(x)
    for k in s:
        print(k[0], str(round((k[1] + 1)/2 * 100)) + '%', round(k[1], 2))

# kule = ['pimeja', 'walo', 'jelo', 'loje', 'laso', 'kasi']
#
# for x in kule:
#     sc(x, 'tenpo')
#     sc(x, 'kule')
#     print(' ')

sc('kili', 'kule')


# most_similar('pimeja')



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
