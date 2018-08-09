import os
import json
import numpy as np
from sklearn import metrics

def load_dataset(x):
    with open('%s.json' % x) as f:
        return json.load(f)

def __get_unique_values_from_key(d, k):
    u = set()
    for dp in d:
        _ = dp[k]
        if(type(_) == list): 
            for __ in _: u.add(__)
        else: u.add(_)
    return list(u)


def categories(data):
    return __get_unique_values_from_key(data, 'categories')

def industries(data):
    return __get_unique_values_from_key(data, 'industries')

def exp_levels(data):
    return __get_unique_values_from_key(data, 'experience')

def evaluate(c, t, e):
    p = c.predict(t)
    return np.mean(p == e)

def analyze(c, t, e, n):
    return metrics.classification_report(e, c.predict(t), n)