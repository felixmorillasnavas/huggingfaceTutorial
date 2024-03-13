from Levenshtein import distance

text_one = "I lova apples"
text_two = "I love oranges"

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


def jaccard_distance(tokens1, tokens2):
    intersection = tokens1.intersection(tokens2)
    union = tokens1.union(tokens2)
    return 1 - (len(intersection) / len(union))


distance_text = jaccard_distance(tokens1, tokens2)
print(f"Jaccard Distance: {distance_text}")


def levenshtein_distance(text1, text2):
    return distance(text1, text2)


distance_text = levenshtein_distance(text_one, text_two)
print(f"Levenshtein Distance: {distance_text}")
