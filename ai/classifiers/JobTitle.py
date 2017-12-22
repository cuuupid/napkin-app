from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


def vectorize(data):
    cv = CountVectorizer()
    return cv.fit_transform([_['title'] for _ in data])


def frequency(vdata):
    return TfidfTransformer(use_idf=False).fit(vdata).transform(vdata)


def model(fdata, targets):
    return MultinomialNB().fit(fdata, targets)


def pipe(data):
    c = Pipeline([('vzd', CountVectorizer()),
                  ('tfd', TfidfTransformer()),
                  ('clf', MultinomialNB())])
    c.fit([_['title'] for _ in data], [_['categories'][0] for _ in data])
    return c