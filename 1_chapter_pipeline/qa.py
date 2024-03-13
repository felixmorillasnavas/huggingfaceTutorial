from transformers import pipeline

# Specify the model and tokenizer that are compatible
oracle = pipeline(
    "question-answering", model="distilbert-base-cased-distilled-squad",
    tokenizer="distilbert-base-cased"
)

# Your input dictionary remains the same
input_dict = {
    "question": "What is the colour of the dog?",
    "context": "It was a great story about love and loss. Henry and I took a walk in the park. We saw a dog and a cat. The cat was black and the dog was brown. It was a great day."
}

print(oracle(input_dict))

