from flask import request
import json
import numpy as np
from joblib import load
from sklearn.feature_extraction.text import CountVectorizer


clf = load('models/rfmodel.joblib')


def routefunc():
    return "Hello from route.py"


def queryprocess(query):
    f = open('data/dataColumn.txt', 'r').read()
    v = json.loads(f)

    qvec = np.zeros(len(v)-1)
    for word in query:
        if word in v:
            qvec[v.index(word)] += 1
    return qvec


def prediction():
    data = json.loads(request.data)
    query = data["query"]
    query = [' '.join(map(str, query))]

    ab = CountVectorizer()
    ab.fit_transform(query)

    qvec = [queryprocess(ab.get_feature_names())]

    predictions = clf.predict(qvec)

    print(predictions)
    data = {"result": predictions[0], "error": ""}
    return json.dumps(data)
