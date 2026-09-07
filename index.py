#-------------------------------------------------------------------------
# AUTHOR: Parth Patel
# FILENAME: index.py
# SPECIFICATION: Inverted Index
# FOR: CS 4250 - Assignment #1
# TIME SPENT: 2 hrs
#-------------------------------------------------------------------------

import pandas as pd

# Reading the document collection
data = pd.read_csv("collection.csv")

# Defining the dictionary used for lemmatization
lemmas = {
    "homes": "home",
    "home": "home",
    "sales": "sale",
    "sale": "sale",
    "increases": "increase",
    "increasing": "increase",
    "rising": "rise",
    "rise": "rise"
}

# Creating the data structure that will store the inverted index
invertedIndex = {}

# Processing each document in the collection
for i, row in data.iterrows():

    docID = row["Document"]
    text = row["Text"]

    # Applying surface-level normalization
    text = text.lower()

    # Tokenizing the document
    tokens = text.replace(".", "").split()

    # Applying lemmatization
    normalized_tokens = []
    for token in tokens:
        if token in lemmas:
            normalized_tokens.append(lemmas[token])
        else:
            normalized_tokens.append(token)

    # Building the inverted index
    for term in normalized_tokens:
        if term not in invertedIndex:
            invertedIndex[term] = []
        if docID not in invertedIndex[term]:
            invertedIndex[term].append(docID)

# Printing the inverted index with terms ordered alphabetically
for term in sorted(invertedIndex.keys()):
    print(term, ":", invertedIndex[term])
