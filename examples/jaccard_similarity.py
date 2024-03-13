


def tokenize(text):
    return set(text.lower().split())


tokens1 = tokenize(text_one)
tokens2 = tokenize(text_two)


def jaccard_similarity(tokens1, tokens2):
    intersection = tokens1.intersection(tokens2)
    union = tokens1.union(tokens2)
    return len(intersection) / len(union)


similarity = jaccard_similarity(tokens1, tokens2)
print(f"Jaccard Similarity: {similarity}")