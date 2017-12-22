from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier


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
                  ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                        alpha=1e-3, random_state=42,
                                        max_iter=5, tol=None))])
    c.fit([_['title'] for _ in data], [_['categories'][0] for _ in data])
    return c
