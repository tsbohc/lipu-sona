import csv
from nltk import sent_tokenize, word_tokenize

import time
import datetime
import random

import pickle

def load(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def save(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)
    print('saved', filename)

# NB: ale/ali alt spelling, i.e convert ali to ale *before* training the model
# could leave it before grabbing the frequency data though

def process_tatoeba():
    with open('csv/tatoeba/tatoeba.csv') as file:
        reader = csv.DictReader(file)
        tatoeba = []
        for row in reader:
            row_dict = dict(row)
            sents = [word_tokenize(s) for s in sent_tokenize(row_dict['text'])]
            # for i, s in enumerate(sents):
            #     sents[i] = [t for t in s if t.isalpha()]

            tatoeba.append({
                'date': round(datetime.datetime.strptime(row_dict['added'], "%Y-%m-%d %H:%M:%S").timestamp()),
                'body': sents
            })

    return tatoeba

def process_submissions():
    with open('csv/reddit/submissions.csv') as file:
        reader = csv.DictReader(file)
        submissions = []
        for row in reader:
            row_dict = dict(row)

            # FIXME: change single quotes to backticks before tokenising! the
            # tokenizer includes single quotes in words, like for the english "don't" !!!

            sents = [word_tokenize(s) for s in sent_tokenize(row_dict['title'])] + [word_tokenize(s) for s in sent_tokenize(row_dict['selftext'])]

            submissions.append({
                'date': int(row_dict['created_utc']),
                'body': sents
            })

    return submissions


def process_comments():
    with open('csv/reddit/comments.csv') as file:
        reader = csv.DictReader(file)
        comments = []
        for row in reader:
            row_dict = dict(row)

            sents = [word_tokenize(s) for s in sent_tokenize(row_dict['body'])]

            comments.append({
                'date': int(row_dict['created_utc']),
                'body': sents
            })

    return comments


def process_t(filename):
    data = []
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            row_dict = dict(row)

            sents = [word_tokenize(s) for s in sent_tokenize(row_dict['Content'])]

            data.append({
                'date': int(row_dict['Date']),
                'body': sents
            })
    return data

# ---

with open('etymology.csv') as file:
    reader = csv.DictReader(file)
    etymology = []
    for row in reader:
        etymology.append(dict(row))

vocabulary = []

for e in etymology:
    vocabulary.append(e['word'])

def istokipona(w):
    return w in vocabulary

# ---

stop = '{<%-%>}'

def clean(data):
    for d in data:
        for i, s in enumerate(d['body']):
            for j, w in enumerate(s):
                if not istokipona(w):

                    # fix capitalisation
                    if not w.isalpha() and len(w) == 1:
                        #s[j] = '' # clean punctuation later
                        pass
                    elif j == 0:
                        _w = w.lower()
                        if istokipona(_w):
                            w = _w
                            s[j] = _w
                        else:
                            s[j] = stop
                    elif w[0].isupper():
                        s[j] = '' # could get "which words precede proper names" from this
                    else:
                        s[j] = stop


            s = list(filter(lambda w: w != '', s)) # remove empty elements
            d['body'][i] = s

    corpus = []

    for d in data:
        for i, s in enumerate(d['body']):

            consec = []

            for j, w in enumerate(s):
                if w != stop and w.isalpha():
                    consec.append(w)
                if w == stop or j == len(s) - 1:
                    if len(consec) > 3:

                        # fix ms vs s unix timestamps
                        if d['date'] > time.time() + 365 * 24 * 3600:
                            d['date'] = round(d['date']/1000)

                        corpus.append({
                            'date': d['date'],
                            'body': consec
                        })
                    consec = []

    return corpus


dataset = \
        process_tatoeba() + \
        process_submissions() + \
        process_comments() + \
        process_t("csv/t/t-l.csv") + \
        process_t("csv/t/t-n.csv") + \
        process_t("csv/t/t-a.csv") + \
        process_t("csv/t/t-s.csv") + \
        process_t("csv/t/t-m.csv")

corpus = clean(dataset)
random.shuffle(corpus)

# ---

# clear the contents
with open('../corpus', 'w') as f:
    pass

# write the corpus to a file
with open('../corpus', 'a') as f:
    for d in corpus:
        f.write(str(d['date']) + ' ' + ' '.join(d['body']) + '\n')

# or pickle
# save(corpus, 'corpus')
